# -*- coding: utf-8 -*-
import logging

from PyQt4.QtGui import QDialog, QMessageBox, QPrinter

from form_invoice_ui import *
from invoice.bean.beans_op import *
from invoice.common import common_util
from invoice.common import table_util
from invoice.common import money_convert
from invoice.common.settings import Settings
from invoice.gui.common_ui import MyComboBox
from invoice.image import add_text_in_invoice

logger = logging.getLogger(__name__)


class InvoiceDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, id=None):
        super(InvoiceDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.id = id
        self.del_id_list = []
        self.init_ui()
        self.is_saved = False

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
        self.print_and_save_btn = QtGui.QPushButton(u"打印并保存")
        self.buttonBox.addButton(self.print_and_save_btn, QtGui.QDialogButtonBox.ActionRole)
        self.print_and_save_btn.clicked.connect(self.action_print_and_save)

    def init_ui(self):
        # 将发票号码，发票代码，金额大写改为不可编辑
        self.invoice_num_lineEdit.setDisabled(True)
        self.invoice_code_lineEdit.setDisabled(True)
        self.total_num_cn_lineEdit.setDisabled(True)

        # 初始化表格中的选择框
        combo_box = MyComboBox(self.invoice_detail_tableWidget)
        self.invoice_detail_tableWidget.setItemDelegateForColumn(1, combo_box)

        # 初始化客户下拉选择框
        custom_name_combobox = self.custom_name_comboBox
        custom_name_combobox.setEditable(True)
        custom_list = Custom.select().where(Custom.status == 0).order_by(Custom.name)
        for custom in custom_list:
            custom_name_combobox.addItem(custom.name)
        custom_name_combobox.setEditText("")

        # 初始化开票人下拉选择框
        self.drawer_comboBox.setEditable(True)
        self.beneficiary_comboBox.setEditable(True)
        self.reviewer_comboBox.setEditable(True)
        user_list = User.select().order_by(User.name)
        for user in user_list:
            self.drawer_comboBox.addItem(user.name)
            self.beneficiary_comboBox.addItem(user.name)
            self.reviewer_comboBox.addItem(user.name)

        # 默认值为当前用户
        user_id = Settings.value_int(Settings.USER_ID)
        user = User.get(id=user_id)
        self.drawer_comboBox.setEditText(user.name)

    def init_default_data(self):
        """'
        新建发票的时候，在系统中设置默认的数据
        """
        # --------------------------
        # 将当前登录用户作为开票人
        self.beneficiary_comboBox.setEditText(Settings.value_q_str(Settings.BENEFICIARY_NAME))
        self.reviewer_comboBox.setEditText(Settings.value_q_str(Settings.REVIEWER_NAME))
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
            table_util.set_table_item_blank_value(table, i, 0)
            table_util.set_table_item_un_editable(table, i, 0)

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
            self.drawer_comboBox.setEditText(common_util.to_string_trim(invoice.drawer))
            self.beneficiary_comboBox.setEditText(common_util.to_string_trim(invoice.beneficiary))
            self.reviewer_comboBox.setEditText(common_util.to_string_trim(invoice.reviewer))

            # 根据ID查询明细
            invoice_detail_list = list(Invoice.get(id=data_id).invoiceDetails)
            row_count = len(invoice_detail_list)
            invoice_detail_table = self.invoice_detail_tableWidget
            invoice_detail_table.setRowCount(row_count)

            # 将数据加载到表格中
            for i in range(row_count):
                invoice_detail = invoice_detail_list[i]

                table_util.set_table_item_value_editable(invoice_detail_table, i, 0, invoice_detail.id, True)
                table_util.set_table_item_value(invoice_detail_table, i, 1, invoice_detail.product.name)
                table_util.set_table_item_value(invoice_detail_table, i, 2, invoice_detail.product.code)
                table_util.set_table_item_value(invoice_detail_table, i, 3, invoice_detail.pro_num)
                table_util.set_table_item_value(invoice_detail_table, i, 4, invoice_detail.product.unit_price)
                table_util.set_table_item_value(invoice_detail_table, i, 5, invoice_detail.contain_tax_price)
        except Invoice.DoesNotExist:
            logger.exception(u"程序出现异常")

    def accepted(self):
        """
        确定按钮事件
        :return:
        """
        self.save_or_update()
        self.parent.invoice_filter_btn_clicked()

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
            product_name = table.item(row_num, col_num).text()
            product_name = str(product_name).decode("GBK")

            # 查询数据
            try:
                product = Product.get(Product.name == product_name)
            except Exception as e:
                product = None

            # 更新表格
            if product:
                table_util.set_table_item_value(table, row_num, 2, product.code)
                table_util.set_table_item_value(table, row_num, 4, product.unit_price)

        # 如果是单价和数量更新，则重新计算总金额
        if col_num == 3 or col_num == 4:
            self.caclulate_product_price(row_num)

        # 如果是单个产品金额更新，则
        if col_num == 5:
            self.caclulate_all_product_price()

    def action_print_and_save(self):
        """
        确定按钮事件
        :return:
        """
        if not self.is_saved:
            self.is_saved = True
            self.print_and_save_btn.setDisabled(True)
            self.save_or_update()
            self.print_by_id()
            self.parent.invoice_filter_btn_clicked()
            self.close()

    def check_invoice(self):
        data_id = self.id

        # 总金额
        invoice = Invoice.get(id=data_id)
        total_num = invoice.total_num

        # 汇总金额
        total_num_all = 0
        tatal_product_id = {}
        invoice_detail_list = list(Invoice.get(id=data_id).invoiceDetails)
        for invoice_detail in invoice_detail_list:
            # 总金额
            contain_tax_price = invoice_detail.contain_tax_price
            total_num_all += contain_tax_price

            # 产品出现次数
            product_id = invoice_detail.product.id
            if tatal_product_id.has_key(product_id):
                current_num = tatal_product_id[product_id] + 1
                tatal_product_id[product_id] = current_num
            else:
                tatal_product_id[product_id] = 1

        if total_num_all != total_num:
            QMessageBox.information(self.parentWidget(), "Information", u'总金额[{0}]与明细汇总金额[{1}]不一致！'.format(total_num, total_num_all))
            return False

        for key in tatal_product_id:
            if tatal_product_id[key] > 1:
                QMessageBox.information(self.parentWidget(), "Information", u'明细中存在两条相同的产品！')
                return False

        return True

    def action_add_invoice_detail(self):
        """
        添加一个空白列
        """
        table = self.invoice_detail_tableWidget
        row_count = table.rowCount()
        table.insertRow(row_count)
        table_util.set_table_item_value(table, row_count, 3, "1")
        table_util.set_table_item_blank_value(table, row_count, 0)
        table_util.set_table_item_un_editable(table, row_count, 0)

    def action_del_invoice_detail(self):
        """
        删除选中的列
        """
        table = self.invoice_detail_tableWidget
        selected_rows = table_util.get_selected_row_number_list(table)
        for row_count in selected_rows:
            detail_id = table_util.get_item_value(table, row_count, 0)
            table.removeRow(row_count)
            if detail_id is not None and len(detail_id) > 0:
                self.del_id_list.append(detail_id)
            self.caclulate_all_product_price()

    def caclulate_product_price(self, row_num):
        """
        计算本行数据的总金额
        :param row_num:行数
        :return:
        """
        table = self.invoice_detail_tableWidget
        pro_num = table_util.get_item_value_int(table, row_num, 3)
        product_unit_price = table_util.get_item_value_float(table, row_num, 4)

        product_price = pro_num * product_unit_price
        table_util.set_table_item_value(table, row_num, 5, str(product_price))

    def caclulate_all_product_price(self):
        """
        将所有行的总金额加起来
        :return:
        """
        table = self.invoice_detail_tableWidget
        row_count = table.rowCount()

        total_num = 0
        for i in range(row_count):
            product_price = table_util.get_item_value_float(table, i, 5)
            total_num += product_price
        self.total_num_lineEdit.setText(str(total_num))

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

    def save_or_update(self):
        try:
            invoice_num = table_util.get_edit_text(self.invoice_num_lineEdit)
            invoice_code = table_util.get_edit_text(self.invoice_code_lineEdit)
            custom_name = self.custom_name_comboBox.currentText()
            total_num = table_util.get_edit_text_float(self.total_num_lineEdit)
            drawer = self.drawer_comboBox.currentText()
            beneficiary = self.beneficiary_comboBox.currentText()
            reviewer = self.reviewer_comboBox.currentText()

            # 保存用户信息
            custom_of_this = save_or_update_custom(custom_name)

            # 保存发票信息
            invoice = Invoice()
            invoice.id = self.id
            invoice.invoice_num = invoice_num
            invoice.invoice_code = invoice_code
            invoice.total_num = total_num
            invoice.drawer = drawer
            invoice.beneficiary = beneficiary
            invoice.reviewer = reviewer
            invoice.custom = custom_of_this
            invoice = save_or_update_invoice(invoice)
            self.id = invoice.id

            if len(self.del_id_list) > 0:
                q = InvoiceDetail.delete().where(InvoiceDetail.id << self.del_id_list)
                q.execute()

            # 保存发票明细
            table = self.invoice_detail_tableWidget
            row_count = table.rowCount()
            for i in range(row_count):
                detail_id = table_util.get_item_value(table, i, 0)
                product_name = table_util.get_item_value(table, i, 1)
                product_code = table_util.get_item_value(table, i, 2)
                pro_num = table_util.get_item_value_float(table, i, 3)
                product_unit_price = table_util.get_item_value_float(table, i, 4)
                contain_tax_price = table_util.get_item_value_float(table, i, 5)

                if product_name:
                    # 获取产品信息
                    product_of_this = save_or_update_product(product_name, product_code, product_unit_price)

                    invoice_detail = InvoiceDetail()
                    invoice_detail.id = detail_id
                    invoice_detail.pro_num = pro_num
                    invoice_detail.contain_tax_price = contain_tax_price
                    invoice_detail.product = product_of_this
                    invoice_detail.invoice = invoice
                    save_or_update_invoice_detail(invoice_detail)
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.exception(u"报错客户信息出错！")
            logger.error(e)

    def print_by_id(self):
        invoice_id = self.id

        # 将合同信息填充到模板中
        # TODO 文件路径写死了

        img_path = "D:\\123333.jpg"
        in_img_path = config.PROGRAM_PATH + "\\" + config.PATH_OF_INVOICE_TEMPLATE_BLANK
        add_text_in_invoice.add_text_in_image(img_path, invoice_id, in_img_path=in_img_path)
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
