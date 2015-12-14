# -*- coding: utf-8 -*-
import logging

from PyQt4.QtCore import QModelIndex, QVariant
from PyQt4.QtGui import QDialog, QStandardItemModel, QMessageBox, QPrinter

from form_invoice_ui import *
from invoice.bean.beans import *
from invoice.common import common_util
from invoice.common import table_util
from invoice.common import money_convert
from invoice.common.settings import Settings
from invoice.gui.common_ui import DBComboBoxDelegate
from invoice.image import add_text_in_invoice

logger = logging.getLogger(__name__)

class InvoiceDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, id=None):
        super(InvoiceDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.id = id
        self.init_product_combo_data()

        # 初始化数据
        if id:
            self.init_data(id)
        else:
            self.init_default_data()

        # 绑定事件
        self.buttonBox.accepted.connect(self.accepted)
        self.connect(self.invoice_detail_tableWidget, QtCore.SIGNAL('cellChanged(int,int)'), self.action_cell_changed)
        self.total_num_lineEdit.textChanged.connect(self.action_total_num_text_changed)
        self.add_invoice_detail_btn.clicked.connect(self.action_add_invoice_detail)
        self.del_invoice_detail_btn.clicked.connect(self.action_del_invoice_detail)

        # 添加打印并保存按钮
        print_and_save_btn = QtGui.QPushButton(u"打印并保存")
        self.buttonBox.addButton(print_and_save_btn, QtGui.QDialogButtonBox.ActionRole)
        print_and_save_btn.clicked.connect(self.action_print_and_save)

    def action_add_invoice_detail(self):
        pass
        print "action_add_invoice_detail"

    def action_del_invoice_detail(self):
        pass
        print "action_add_invoice_detail"

    def init_default_data(self):
        """'
        新建发票的时候，在系统中设置默认的数据
        """
        # --------------------------
        # 将当前登录用户作为开票人
        user_id = Settings.value(Settings.USER_ID).toInt()[0]
        user = User.get(id=user_id)
        self.drawer_lineEdit.setText(user.name)
        self.beneficiary_lineEdit.setText(Settings.value_q_str(Settings.BENEFICIARY_NAME))
        self.reviewer_lineEdit.setText(Settings.value_q_str(Settings.REVIEWER_NAME))
        self.invoice_code_lineEdit.setText(Settings.value_str(Settings.INVOICE_CODE))
        # --------------------------

        # --------------------------
        # 设置发票号码
        # TODO 性能优化
        invoice_start_num = Settings.value_int(Settings.INVOICE_START_NUM)
        invoice_end_num = Settings.value_int(Settings.INVOICE_END_NUM)
        # 查询号段内的数据，并获取已使用数量
        invoice_list = Invoice.select(Invoice.invoice_num).where(
            Invoice.invoice_num.between(invoice_start_num, invoice_end_num)).order_by(Invoice.invoice_num.asc())
        if invoice_list and len(invoice_list) > 0:
            # 如果有值，则下一个为最大的一个
            invoice = list(invoice_list)[-1]
            invoice_current_num = invoice.invoice_num + 1
        else:
            # 如果无值，则下一个为起始值
            invoice_current_num = invoice_start_num
        # 将最新值添加到输入框中
        self.invoice_num_lineEdit.setText(str(invoice_current_num))
        # --------------------------

        # --------------------------
        # 将明细添加到表格中
        table = self.invoice_detail_tableWidget
        row_count = table.rowCount()
        for i in range(row_count):
            table_util.set_table_item_value(table, i, 3, "1")
            # table_util.set_table_item_value_editable(table, i, 0, "", True)
            # TODO ID不可编辑
            # table_util.set_table_item_un_editable(table, i, 0)
        # --------------------------

    def init_data(self, data_id):
        """
        根据发票ID，将发票的信息初始化到Dialog中
        :param data_id:发票ID
        :return:
        """
        try:
            # 设置发票信息
            invoice = Invoice.get(id=data_id)
            self.invoice_num_lineEdit.setText(common_util.to_string_trim(invoice.invoice_num))
            self.invoice_code_lineEdit.setText(common_util.to_string_trim(invoice.invoice_code))
            self.custom_name_comboBox.setEditText(common_util.to_string_trim(invoice.custom.name))
            self.total_num_lineEdit.setText(common_util.to_string_trim(invoice.total_num))
            total_num_cn = money_convert.to_rmb_upper(invoice.total_num)
            self.total_num_cn_lineEdit.setText(common_util.to_string_trim(total_num_cn))
            self.drawer_lineEdit.setText(common_util.to_string_trim(invoice.drawer))
            self.beneficiary_lineEdit.setText(common_util.to_string_trim(invoice.beneficiary))
            self.reviewer_lineEdit.setText(common_util.to_string_trim(invoice.reviewer))

            # 根据ID查询明细
            invoice_detail_list = list(Invoice.get(id=data_id).invoiceDetails)
            row_count = len(invoice_detail_list)
            invoice_detail_table = self.invoice_detail_tableWidget
            invoice_detail_table.setRowCount(row_count)

            # 将数据加载到表格中
            for i in range(row_count):
                invoice_detail = invoice_detail_list[i]

                table_util.set_table_item_value_editable(invoice_detail_table, i, 0, invoice_detail.id, True)
                table_util.set_table_item_value(invoice_detail_table, i, 1, invoice_detail.product.code)
                table_util.set_table_item_value(invoice_detail_table, i, 2, invoice_detail.product.name)
                table_util.set_table_item_value(invoice_detail_table, i, 3, invoice_detail.pro_num)
                table_util.set_table_item_value(invoice_detail_table, i, 4, invoice_detail.product.unit_price)
                table_util.set_table_item_value(invoice_detail_table, i, 5, invoice_detail.contain_tax_price)
        except Invoice.DoesNotExist:
            logger = logging.getLogger(__name__)
            logger.exception(u"程序出现异常")

    def init_product_combo_data(self):
        """
        初始产品下拉选择框
        :return:
        """
        self.invoice_num_lineEdit.setDisabled(True)
        self.invoice_code_lineEdit.setDisabled(True)
        self.total_num_cn_lineEdit.setDisabled(True)

        combo_box = DBComboBoxDelegate(self.invoice_detail_tableWidget)
        self.invoice_detail_tableWidget.setItemDelegateForColumn(1, combo_box)

        # 初始化客户数据
        custom_name_combobox = self.custom_name_comboBox
        custom_name_combobox.setEditable(True)
        custom_list = Custom.select().where(Custom.status == 0).order_by(Custom.name)
        for custom in custom_list:
            custom_name_combobox.addItem(custom.name)
        custom_name_combobox.setEditText("")

    def action_total_num_text_changed(self, string):
        """
        绑定数字金额修改事件
        :param string:数字金额
        :return:
        """
        try:
            total_num = float(string)
            total_num_cn = money_convert.to_rmb_upper(total_num)
            self.total_num_cn_lineEdit.setText(common_util.to_string_trim(total_num_cn))
        except ValueError:
            QMessageBox.information(self.parentWidget(), u"错误", u'请输入数字金额！')

    def action_cell_changed(self, row_num, col_num):
        """
        绑定表格中元素修改事件
        :param row_num:行数
        :param col_num:列数
        :return:
        """
        table = self.invoice_detail_tableWidget

        # 如果产品编码更新
        if col_num == 1:
            product_code = table.item(row_num, col_num).text()

            # 查询数据
            product = Product.get(code=product_code)

            # 更新表格
            table_util.set_table_item_value(table, row_num, 2, product.name)
            table_util.set_table_item_value(table, row_num, 4, product.unit_price)

        # 如果是单价和数量更新，则重新计算总金额
        if col_num == 3 or col_num == 4:
            self.caculate_price()

    def caculate_price(self):
        """
        根据表格中的元素计算总金额
        :return:
        """
        table = self.invoice_detail_tableWidget
        row_count = table.rowCount()

        total_num = 0
        for i in range(row_count):
            pro_num = table_util.get_item_value_int(table, i, 3)
            product_unit_price = table_util.get_item_value_float(table, i, 4)

            product_price = pro_num * product_unit_price
            table_util.set_table_item_value(table, i, 5, str(product_price))
            total_num += product_price

        self.total_num_lineEdit.setText(str(total_num))

    def add_invoice(self):
        """
        添加发票信息
        :return:
        """
        invoice_num = table_util.get_edit_text(self.invoice_num_lineEdit)
        invoice_code = table_util.get_edit_text(self.invoice_code_lineEdit)
        custom_name = self.custom_name_comboBox.currentText()
        total_num = table_util.get_edit_text_float(self.total_num_lineEdit)
        drawer = table_util.get_edit_text(self.drawer_lineEdit)
        beneficiary = table_util.get_edit_text(self.beneficiary_lineEdit)
        reviewer = table_util.get_edit_text(self.reviewer_lineEdit)

        # 保存用户信息
        try:
            custom_of_this = Custom.get(name=custom_name)
        except Exception:
            custom_of_this = Custom.create(name=custom_name)
            custom_of_this.save()

        # 保存发票信息
        invoice = Invoice.create(invoice_num=invoice_num,
                                 invoice_code=invoice_code,
                                 total_num=total_num,
                                 drawer=drawer,
                                 beneficiary=beneficiary,
                                 reviewer=reviewer,
                                 custom=custom_of_this)
        invoice.save()
        self.id = invoice.id

        # 保存发票明细
        table = self.invoice_detail_tableWidget
        row_count = table.rowCount()
        for i in range(row_count):
            product_code = table_util.get_item_value(table, i, 1)
            pro_num = table_util.get_item_value_float(table, i, 3)
            contain_tax_price = table_util.get_item_value_float(table, i, 5)

            if product_code:
                # 获取产品信息
                product_of_this = Product.get(code=product_code)

                invoice_detail = InvoiceDetail.create(
                    pro_num=pro_num,
                    contain_tax_price=contain_tax_price,
                    product=product_of_this,
                    invoice=invoice
                )
                invoice_detail.save()

    def update_invoice(self):
        """
        修改发票信息
        :return:
        """
        invoice_num = table_util.get_edit_text(self.invoice_num_lineEdit)
        invoice_code = table_util.get_edit_text(self.invoice_code_lineEdit)
        custom_name = self.custom_name_comboBox.currentText()
        total_num = table_util.get_edit_text_float(self.total_num_lineEdit)
        drawer = table_util.get_edit_text(self.drawer_lineEdit)
        beneficiary = table_util.get_edit_text(self.beneficiary_lineEdit)
        reviewer = table_util.get_edit_text(self.reviewer_lineEdit)

        # 保存用户信息
        try:
            custom_of_this = Custom.get(name=custom_name)
        except Exception:
            custom_of_this = Custom.create(name=custom_name)
            custom_of_this.save()

        # 保存发票信息
        q = Invoice.update(invoice_num=invoice_num,
                           invoice_code=invoice_code,
                           total_num=total_num,
                           drawer=drawer,
                           beneficiary=beneficiary,
                           reviewer=reviewer,
                           custom=custom_of_this).where(Invoice.id == self.id)
        q.execute()

        # 保存发票明细
        table = self.invoice_detail_tableWidget
        row_count = table.rowCount()
        for i in range(row_count):
            detail_id = table_util.get_item_value(table, i, 0)
            product_code = table_util.get_item_value(table, i, 1)
            product_name = table_util.get_item_value(table, i, 2)
            pro_num = table_util.get_item_value_float(table, i, 3)
            product_unit_price = table_util.get_item_value_float(table, i, 4)
            contain_tax_price = table_util.get_item_value_float(table, i, 5)

            if product_code:
                # 获取产品信息
                product_of_this = Product.get(code=product_code)

                if detail_id:
                    q = InvoiceDetail.update(pro_num=pro_num,
                                             contain_tax_price=contain_tax_price,
                                             product=product_of_this
                                             ).where(InvoiceDetail.id == detail_id)
                    q.execute()

    def accepted(self):
        """
        确定按钮事件
        :return:
        """
        self.save_or_update()
        self.parent.invoice_filter_btn_clicked()

    def save_or_update(self):
        try:
            if self.id:
                self.update_invoice()
            else:
                self.add_invoice()
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.exception(u"报错客户信息出错！")
            logger.error(e)

    def action_print_and_save(self):
        """
        确定按钮事件
        :return:
        """
        self.save_or_update()
        self.print_by_id()
        self.parent.invoice_filter_btn_clicked()

    def print_by_id(self):
        invoice_id = self.id

        # 将合同信息填充到模板中
        # TODO 文件路径写死了
        img_path = "D:\\123333.jpg"
        add_text_in_invoice.add_text_in_image(img_path, invoice_id, in_img_path=config.PATH_OF_INVOICE_TEMPLATE)
        logger.info(u"生成图片成功，路径{0}".format(img_path))

        # TODO 处理打印失败的情况
        # 弹出打印框
        printer = QPrinter(QPrinter.HighResolution)
        print_dialog = QtGui.QPrintDialog(printer, self)
        print_dialog.setWindowTitle("打印发票")

        if print_dialog.exec_() == QtGui.QDialog.Accepted:
            # 如果在弹出的打印界面中选择了打印
            self.parent.print_invoice_pic(printer)

            # 此处无法监控到打印是否成功
            q = Invoice.update(status=1, start_time=datetime.datetime.now()).where(Invoice.id == invoice_id)
            q.execute()
            self.parent.show_msg_at_rigth_label(u"已经开始打印，由于无法监控是否打印成功，如果打印失败，请重新补打！")

            # 关闭Dialog
            self.accept()
        del print_dialog
