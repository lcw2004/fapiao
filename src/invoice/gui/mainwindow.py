# -*- coding: utf-8 -*-
import logging

from PyQt4.QtCore import Qt, QString, QSize, QSizeF
from PyQt4.QtGui import QMainWindow, QMessageBox, QAbstractItemView, QPrinter, QPrintPreviewDialog, QPainter
from PyQt4 import QtCore
from PyQt4 import QtGui

from invoice.common.excel_writer import InvoiceElsxExporter
from invoice.gui.form_custom import CustomDialog
from invoice.gui.form_invoice import InvoiceDialog
from invoice.gui.form_product import ProductDialog
from invoice.gui.form_section import SectionDialog
from invoice.gui.form_user import UserDialog
from invoice.gui.menu_config import MenuConfigDialog
from invoice.image import add_text_in_invoice
from mainwindow_ui import Ui_MainWindow
from invoice.sys import invoice_exporter
from invoice.common import excel_parser
from invoice.common import table_util
from invoice.common.settings import Settings
from invoice.bean.beans import *

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.showMaximized()

        # =====================
        # Excel导入
        self.connect(self.excel_selectl_file_btn, QtCore.SIGNAL("clicked()"), self.excel_select_file_btn_clicked)
        self.connect(self.excel_gen_invoice_btn, QtCore.SIGNAL("clicked()"), self.excel_gen_invoice_btn_clicked)
        # =====================

        # =====================
        # 临时待处理数据
        self.connect(self.invoice_filter_btn, QtCore.SIGNAL("clicked()"), self.invoice_filter_btn_clicked)
        self.connect(self.invoice_table, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.invoice_table_item_clicked)
        self.connect(self.invoice_add_btn, QtCore.SIGNAL("clicked()"), self.invoice_add_btn_clicked)
        self.connect(self.invoine_update_btn, QtCore.SIGNAL("clicked()"), self.invoice_update_btn_clicked)
        self.connect(self.invoice_delete_btn, QtCore.SIGNAL("clicked()"), self.invoice_delete_btn_clicked)
        self.connect(self.invoice_import_xml_btn, QtCore.SIGNAL("clicked()"), self.invoice_import_xml_btn_clicked)
        self.connect(self.invoice_merge_btn, QtCore.SIGNAL("clicked()"), self.invoice_merge_btn_clicked)
        self.connect(self.invoice_merge_product_btn, QtCore.SIGNAL("clicked()"), self.invoice_merge_product_btn_clicked)
        self.connect(self.invoice_chaifeng_btn, QtCore.SIGNAL("clicked()"), self.invoice_chaifeng_btn_clicked)
        self.connect(self.invoice_print_btn, QtCore.SIGNAL("clicked()"), self.invoice_print_btn_clicked)
        # =====================

        # =====================
        # 已开发票管理
        self.connect(self.ok_invoice_filter_btn, QtCore.SIGNAL("clicked()"), self.ok_invoice_filter_btn_clicked)
        self.connect(self.ok_invoice_table, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'),self.ok_invoice_table_item_clicked)
        self.connect(self.ok_invoice_export_btn, QtCore.SIGNAL("clicked()"), self.ok_invoice_export_btn_clicked)
        self.connect(self.ok_invoice_print_btn, QtCore.SIGNAL("clicked()"), self.ok_invoice_print_btn_clicked)
        # =====================

        # =====================
        # 客户管理模块
        self.connect(self.custom_query_btn, QtCore.SIGNAL("clicked()"), self.custom_query_btn_clicked)
        self.connect(self.custom_add_btn, QtCore.SIGNAL("clicked()"), self.custom_add_btn_clicked)
        self.connect(self.custom_update_btn, QtCore.SIGNAL("clicked()"), self.custom_update_btn_clicked)
        self.connect(self.custom_delete_btn, QtCore.SIGNAL("clicked()"), self.custom_delete_btn_clicked)
        # =====================

        # =====================
        # 产品管理模块
        self.connect(self.product_query_btn, QtCore.SIGNAL("clicked()"), self.product_query_btn_clicked)
        self.connect(self.product_add_btn, QtCore.SIGNAL("clicked()"), self.product_add_btn_clicked)
        self.connect(self.product_update_btn, QtCore.SIGNAL("clicked()"), self.product_update_btn_clicked)
        self.connect(self.product_delete_btn, QtCore.SIGNAL("clicked()"), self.product_delete_btn_clicked)
        # =====================

        # =====================
        # 号段管理表（管理员）
        self.connect(self.section_query_btn, QtCore.SIGNAL("clicked()"), self.section_query_btn_clicked)
        self.connect(self.section_add_btn, QtCore.SIGNAL("clicked()"), self.section_add_btn_clicked)
        self.connect(self.section_update_btn, QtCore.SIGNAL("clicked()"), self.section_update_btn_clicked)
        self.connect(self.section_delete_btn, QtCore.SIGNAL("clicked()"), self.section_delete_btn_clicked)
        # =====================

        # =====================
        # 用户管理表（管理员）
        self.connect(self.user_query_btn, QtCore.SIGNAL("clicked()"), self.user_query_btn_clicked)
        self.connect(self.user_add_btn, QtCore.SIGNAL("clicked()"), self.user_add_btn_clicked)
        self.connect(self.user_update_btn, QtCore.SIGNAL("clicked()"), self.user_update_btn_clicked)
        self.connect(self.user_delete_btn, QtCore.SIGNAL("clicked()"), self.user_delete_btn_clicked)
        # =====================

        # =====================
        # 号段管理表（管理员）
        self.actionAbout.triggered.connect(self.action_about)
        self.actionConfig.triggered.connect(self.action_config)
        # =====================

    def action_config(self):
        dialog = MenuConfigDialog(self)
        dialog.show()

    def action_about(self):
        QtGui.QMessageBox.about(self, u"关于",
                config.PRODUCT_ALL_NAME + "\n" +
                "Copyright " + config.PRODUCT_COMPANY)

    def show_msg_at_rigth_label(self, msg):
        self.right_status_label.setText(msg)

    def init_home_page(self):
        invoice_start_num = Settings.value_int(Settings.INVOICE_START_NUM)
        invoice_end_num = Settings.value_int(Settings.INVOICE_END_NUM)

        # --------------------------
        # 查询号段内的数据，并获取已使用数量
        # TODO 性能优化
        invoice_list = Invoice.select(Invoice.invoice_num).where(
            Invoice.invoice_num.between(invoice_start_num, invoice_end_num)).order_by(Invoice.invoice_num.asc())
        if invoice_list and len(invoice_list) > 0:
            # 如果有值，则下一个为最大的一个
            invoice = list(invoice_list)[-1]
            invoice_current_num = invoice.invoice_num + 1
            used_count = len(invoice_list)
        else:
            # 如果无值，则下一个为起始值
            invoice_current_num = invoice_start_num
            used_count = 0
        # --------------------------

        # --------------------------
        # 设置号段信息
        if invoice_start_num > 0 and invoice_end_num > 0:
            all_count = invoice_end_num - invoice_start_num + 1
            last_count = all_count - used_count
            current_section = u"{0} -> {1} , 共计{2}张".format(invoice_start_num, invoice_end_num, all_count)
            self.home_page_current_section_lable.setText(current_section)

            # 普通用户使用情况
            self.home_page_next_num_lable.setText(QString.number(invoice_current_num))
            self.home_page_used_count_lable.setText(QString.number(used_count))
            self.home_page_last_count_lable.setText(QString.number(last_count))

            # 库存管理员使用情况
            use_num = 0
            for no_section in NoSection.select():
                use_num += no_section.end_num - no_section.start_num + 1
            last_num = all_count - use_num
            section_use_status = u"当前号段：{0} -> {1} 共计 {2} 张 ".format(invoice_start_num, invoice_end_num, all_count)
            section_use_status += u" 已经分配 {0} 张，剩余 {1} 张发票".format(use_num, last_num)
            self.section_use_status_label.setText(section_use_status)
        # --------------------------

    def init_ui(self):
        self.setWindowTitle(config.PRODUCT_ALL_NAME)

        # 初始化时间查询条件
        self.init_time_edit(self.ok_invoice_start_time_edit)
        self.init_time_edit(self.ok_invoice_end_time_edit)
        self.ok_invoice_start_time_edit.setDate(datetime.date.today() - datetime.timedelta(days=30))
        self.ok_invoice_end_time_edit.setDate(datetime.date.today() + datetime.timedelta(days=1))

        # 加载首页
        self.init_home_page()

        # =====================
        # 状态栏信息
        status = ""
        user_id = Settings.value_int(Settings.USER_ID)
        user = User.get(id=user_id)
        status += u"当前用户：" + user.name
        self.left_status_label.setText(status)
        # =====================

        # =====================
        # 设置定位到开票页面
        self.tabWidget.setCurrentIndex(1)
        # 根据用户权限，控制是否显示“库存管理”
        if not user.is_admin:
            self.tabWidget.removeTab(5)
        # =====================

    def init_time_edit(self, time_edit):
        time_edit.setDate(QtCore.QDate.currentDate())
        time_edit.setCalendarPopup(True)
        time_edit.setDisplayFormat(u'yyyy年MM月dd日')
        time_edit.cal = time_edit.calendarWidget()
        time_edit.cal.setFirstDayOfWeek(QtCore.Qt.Monday)
        time_edit.cal.setHorizontalHeaderFormat(QtGui.QCalendarWidget.SingleLetterDayNames)
        time_edit.cal.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        time_edit.cal.setGridVisible(True)

    def invoice_merge_product_btn_clicked(self):
        pass

    def invoice_merge_btn_clicked(self):
        invoice_table = self.invoice_table

        # 判断选择的合并的发票数量
        selected_rows = table_util.get_selected_row_number_list(invoice_table)
        if len(selected_rows) <= 1:
            QMessageBox.information(self.parentWidget(), "Information", u'请选择至少两个需要合并的发票！')
            return

        # 获取所有需要合并的行的ID
        invoice_id_list = []
        custom_name_list = []
        for row_num in selected_rows:
            invoice_id = table_util.str_to_unicode_str(invoice_table.item(row_num, 0).text())
            invoice_custom_name = table_util.str_to_unicode_str(invoice_table.item(row_num, 2).text())
            if invoice_id:
                invoice_id_list.append(int(invoice_id))
                custom_name_list.append(invoice_custom_name)

        # 判断是否
        custom_name_set = set(custom_name_list)
        if len(custom_name_set) > 1:
            QMessageBox.information(self.parentWidget(), "Information", u'所选发票中存在两个不同客户的发票！')
            return

        # 将所选发票的详细信息合并到第一个中，并删除其他发票
        main_invoice_id = invoice_id_list[0]
        main_invoice = Invoice.get(id=main_invoice_id)
        q = InvoiceDetail.update(invoice=main_invoice).where(InvoiceDetail.invoice << invoice_id_list[1:])
        q.execute()
        q = Invoice.update(status=9).where(Invoice.id << invoice_id_list[1:])
        q.execute()

        # TODO 重新统计税额
        # invoiceDao.proofreadInvoince(main_invoice_id)

        # 合并成功并刷新表格
        QMessageBox.information(self.parentWidget(), "Information", u'合并成功！')
        self.invoice_filter_btn_clicked()

    def invoice_chaifeng_btn_clicked(self):
        invoice_detail_table = self.invoice_detail_table

        # 判断选择的合并的发票数量
        selected_rows = table_util.get_selected_row_number_list(invoice_detail_table)
        if len(selected_rows) < 1:
            QMessageBox.information(self.parentWidget(), "Information", u'请选择至少一个需要拆分的发票明细！')
            return

        # 获取所有需要合并的行的ID
        invoice_id_list = []
        for row_num in selected_rows:
            invoice_id = table_util.str_to_unicode_str(invoice_detail_table.item(row_num, 0).text())
            if invoice_id:
                invoice_id_list.append(int(invoice_id))

        # 获取发票ID
        if invoice_id_list:
            print invoice_id_list
            invoice_detail = InvoiceDetail.get(id=invoice_id_list[0])
            invoice = invoice_detail.invoice

            new_invoice = Invoice.create(invoice_num=invoice.invoice_num,
                                         remark=invoice.remark,
                                         total_not_tax=invoice.total_not_tax,
                                         custom=invoice.custom)
            new_invoice.save()

            q = InvoiceDetail.update(invoice=new_invoice).where(InvoiceDetail.id << invoice_id_list)
            print q
            q.execute()

            # TODO 重新统计税额
            # invoiceDao.proofreadInvoince(newInvoiceId)
            # invoiceDao.proofreadInvoince(oldInvoiceId)
            QMessageBox.information(self.parentWidget(), "Information", u'拆分成功！')
            self.invoice_filter_btn_clicked()

    def invoice_print_btn_clicked(self):
        invoice_table = self.invoice_table
        self.print_select_invoice(invoice_table)
        self.invoice_filter_btn_clicked()

    def ok_invoice_print_btn_clicked(self):
        invoice_table = self.ok_invoice_table
        self.print_select_invoice(invoice_table)
        self.ok_invoice_filter_btn_clicked()

    def print_select_invoice(self, invoice_table):
        # 获得选中的合同的ID
        selected_rows = table_util.get_selected_row_number_list(invoice_table)
        if len(selected_rows) != 1:
            QMessageBox.information(self, "Information", u'请选择需要打印的合同，每次只能打印一条！')
            return
        invoice_id = table_util.str_to_unicode_str(invoice_table.item(selected_rows[0], 0).text())

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
            self.print_invoice_pic(printer)

            # 此处无法监控到打印是否成功
            q = Invoice.update(status=1, start_time=datetime.datetime.now()).where(Invoice.id == invoice_id)
            q.execute()
            self.show_msg_at_rigth_label(u"已经开始打印，由于无法监控是否打印成功，如果打印失败，请重新补打！")
        del print_dialog

    def print_preview_select_invoice(self, invoice_table):
        # 获得选中的合同的ID
        selected_rows = table_util.get_selected_row_number_list(invoice_table)
        if len(selected_rows) != 1:
            QMessageBox.information(self, "Information", u'请选择需要打印的合同，每次只能打印一条！')
            return
        invoice_id = table_util.str_to_unicode_str(invoice_table.item(selected_rows[0], 0).text())

        # 将合同信息填充到模板中
        # TODO 文件路径写死了
        img_path = "D:\\123333.jpg"
        add_text_in_invoice.add_text_in_image(img_path, invoice_id, in_img_path=config.PATH_OF_INVOICE_TEMPLATE)
        logger.info(u"生成图片成功，路径{0}".format(img_path))

        # 生成打印预览界面
        printer = QPrinter(QPrinter.HighResolution)
        preview = QPrintPreviewDialog(printer, self)
        preview.setMaximumWidth(800)
        preview.setMinimumWidth(800)
        preview.setMaximumHeight(800)
        preview.setMinimumHeight(800)
        preview.paintRequested.connect(self.print_invoice_pic)
        result = preview.exec_()
        if result:
            # 打印成功
            # 修改合同状态和打印的时间
            invoice = Invoice.get(id=invoice_id)
            if invoice.status == 0:
                # 如果合同是未开票状态，将其改为开票状态，并记录开票时间
                q = Invoice.update(status=1, start_time=datetime.datetime.now()).where(Invoice.id == invoice_id)
                q.execute()
                self.show_msg_at_rigth_label(u"开票成功！")
            elif invoice.status == -1 or invoice.status == 1:
                # 如果合同是作废状态或者开票状态，状态不变
                self.show_msg_at_rigth_label(u"补打成功！")
        else:
            # 打印失败
            self.show_msg_at_rigth_label(u"打印失败，请重试！")

    def print_invoice_pic(self, printer):
        logger.info(u"开始打印图片")
        img_path = "D:\\123333.jpg"

        # 设置纸张宽度高度
        width = 7.59
        height = 4.13
        qsize = QSizeF(width, height)
        printer.setPaperSize(qsize, QPrinter.Inch)
        printer.setFullPage(False)

        # 构建Qpainter对象，用于将图片传到打印机上
        painter = QPainter(printer)
        rect = painter.viewport()
        image = QtGui.QPixmap(img_path)
        img_size = image.size()
        img_size.scale(rect.size(), Qt.KeepAspectRatio)  # //此处保证图片显示完整
        painter.setViewport(rect.x(), rect.y(), img_size.width(), img_size.height())
        painter.setWindow(image.rect())
        painter.drawPixmap(0, 0, image)
        logger.info(u"成功加载图片成加载图片")

    def excel_select_file_btn_clicked(self):
        excel_path = QtGui.QFileDialog.getOpenFileName(None, 'Excel', '../', 'Excel File (*.xls)')
        if excel_path:
            logger.debug(u"选择Excel文件:{0}".format(excel_path))
            excel_table_widget = self.excel_table

            # 设置表格头部
            table_util.init_table_headers(excel_table_widget)

            # 解析Excel
            invoice_detail_list = excel_parser.parse_excel_to_invoice_list(excel_path)
            logger.debug(u"解析Excel:{0}".format(invoice_detail_list))

            # 设置表格行数
            row_count = len(invoice_detail_list)
            col_count = 10
            excel_table_widget.setRowCount(row_count)
            excel_table_widget.setColumnCount(col_count)

            # 填充数据
            for i in range(row_count):
                invoice_detail = invoice_detail_list[i]
                table_util.set_table_item_value(excel_table_widget, i, 0, invoice_detail.invoice.custom.name)
                table_util.set_table_item_value(excel_table_widget, i, 1, invoice_detail.invoice.invoice_num)
                table_util.set_table_item_value(excel_table_widget, i, 2, str(invoice_detail.invoice.total_not_tax))
                table_util.set_table_item_value(excel_table_widget, i, 3, invoice_detail.product.type)
                table_util.set_table_item_value(excel_table_widget, i, 4, invoice_detail.product.name)
                table_util.set_table_item_value(excel_table_widget, i, 5, invoice_detail.invoice.remark)

    def excel_gen_invoice_btn_clicked(self):
        excel_table = self.excel_table
        row_count = excel_table.row_count()

        # TODO 判断表格中是否有数据
        if row_count <= 1:
            QMessageBox.information(self.parentWidget(), "Information", u'请先导入发票数据！')
            return

        for i in range(row_count):
            tbl_custom_name = table_util.str_to_unicode_str(excel_table.item(i, 0).text())
            tbl_invoice_invoice_num = table_util.str_to_unicode_str(excel_table.item(i, 1).text())
            tbl_invoice_total_not_tax = table_util.str_to_unicode_str(excel_table.item(i, 2).text())
            tbl_invoice_detail_pro_type = table_util.str_to_unicode_str(excel_table.item(i, 3).text())
            tbl_invoice_detail_pro_name = table_util.str_to_unicode_str(excel_table.item(i, 4).text())
            tbl_invoice_remark = table_util.str_to_unicode_str(excel_table.item(i, 5).text())

            # 保存用户信息
            try:
                custom_of_this = Custom.get(name=tbl_custom_name)
            except Exception:
                custom_of_this = Custom.create(name=tbl_custom_name)
                custom_of_this.save()

            # 保存商品信息
            try:
                product_of_this = Product.get(name=tbl_invoice_detail_pro_name)
            except Exception:
                product_of_this = Product.create(name=tbl_invoice_detail_pro_name, type=tbl_invoice_detail_pro_type)
                product_of_this.save()

            # 保存发票
            invoice_of_this = Invoice.create(invoice_num=tbl_invoice_invoice_num,
                                             remark=tbl_invoice_remark,
                                             total_not_tax=tbl_invoice_total_not_tax,
                                             custom=custom_of_this)
            invoice_of_this.save()

            # 保存发票详细信息
            invoice_detail_of_this = InvoiceDetail.create(
                pro_type=tbl_invoice_detail_pro_type,
                pro_name=tbl_invoice_detail_pro_name,
                not_tax_price=tbl_invoice_total_not_tax,
                invoice_Id=invoice_of_this.id,
                product_id=product_of_this.id,
                invoice=invoice_of_this,
                product=product_of_this
            )
            invoice_detail_of_this.save()

            # TODO 计算税额
            # invoice_detail.caculate()
            # invoiceDao.proofreadInvoince(invoice.id)

        QMessageBox.information(self.parentWidget(), "Information", u'数据已经保存到临时数据区！')
        # TODO 导入成功之后清空数据

    def invoice_filter_btn_clicked(self):
        invoice_list = list(Invoice.select().where(Invoice.status == 0))
        invoice_table = self.invoice_table

        # 设置整行选中
        invoice_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置不可编辑
        invoice_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        row_count = len(invoice_list)
        invoice_table.setRowCount(row_count)

        # 将数据加载到表格中
        for i in range(row_count):
            invoice = invoice_list[i]

            table_util.set_table_item_value(invoice_table, i, 0, invoice.id)
            table_util.set_table_item_value(invoice_table, i, 1, invoice.invoice_num)
            table_util.set_table_item_value(invoice_table, i, 2, invoice.invoice_code)
            table_util.set_table_item_value(invoice_table, i, 4, invoice.total_num)
            table_util.set_table_item_value(invoice_table, i, 5, invoice.drawer)
            table_util.set_table_item_value(invoice_table, i, 6, invoice.beneficiary)
            table_util.set_table_item_value(invoice_table, i, 7, invoice.reviewer)
            table_util.set_table_item_value(invoice_table, i, 8, invoice.total_not_tax)
            table_util.set_table_item_value(invoice_table, i, 9, invoice.total_tax)
            table_util.set_table_item_value(invoice_table, i, 10, invoice.remark)
            table_util.set_table_item_value(invoice_table, i, 14, invoice.serial_number)

            try:
                if invoice.custom:
                    table_util.set_table_item_value(invoice_table, i, 3, invoice.custom.name)
                    table_util.set_table_item_value(invoice_table, i, 11, invoice.custom.code)
                    table_util.set_table_item_value(invoice_table, i, 12, invoice.custom.tax_id)
                    table_util.set_table_item_value(invoice_table, i, 13, invoice.custom.addr)
                    table_util.set_table_item_value(invoice_table, i, 14, invoice.custom.bank_account)
            except Exception:
                pass

    def ok_invoice_filter_btn_clicked(self):
        # 获取查询条件
        start_num = self.ok_invoice_start_num_edit.text()
        end_num = self.ok_invoice_end_num_edit.text()
        start_time = self.ok_invoice_start_time_edit.date().toPyDate()
        end_time = self.ok_invoice_end_time_edit.date().toPyDate()
        logging.info("start_num:" + start_num)
        logging.info("end_num:" + end_num)

        # 查询数据
        if start_num.isEmpty() and not end_num.isEmpty():
            invoice_list = list(Invoice.select().where((Invoice.status == 1) | (Invoice.status == -1),
                                                       Invoice.start_time.between(start_time, end_time),
                                                       Invoice.invoice_num <= end_num))
            logging.info(u"查询")
        elif not start_num.isEmpty() and end_num.isEmpty():
            invoice_list = list(Invoice.select().where((Invoice.status == 1) | (Invoice.status == -1),
                                                       Invoice.start_time.between(start_time, end_time),
                                                       Invoice.invoice_num >= start_num))
            logging.info(u"查询")
        elif start_num.isEmpty() and end_num.isEmpty():
            invoice_list = list(Invoice.select().where((Invoice.status == 1) | (Invoice.status == -1),
                                                       Invoice.start_time.between(start_time, end_time)))
            logging.info(u"查询")
        else:
            invoice_list = list(Invoice.select().where((Invoice.status == 1) | (Invoice.status == -1),
                                                       Invoice.start_time.between(start_time, end_time),
                                                       Invoice.invoice_num.between(start_num, end_num)))
            logging.info(u"查询")
        invoice_table = self.ok_invoice_table

        # 设置整行选中
        invoice_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置不可编辑
        invoice_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        row_count = len(invoice_list)
        invoice_table.setRowCount(row_count)

        # 将数据加载到表格中
        for i in range(row_count):
            invoice = invoice_list[i]

            table_util.set_table_item_value(invoice_table, i, 0, invoice.id)
            if invoice.status == -1:
                table_util.set_table_item_value(invoice_table, i, 1, str(invoice.invoice_num) + u"(作废)")
                table_util.set_table_item_color(invoice_table, i, 1, QtGui.QColor(199, 220, 252))
            else:
                table_util.set_table_item_value(invoice_table, i, 1, invoice.invoice_num)
            table_util.set_table_item_value(invoice_table, i, 2, invoice.invoice_code)
            table_util.set_table_item_value(invoice_table, i, 4, invoice.total_num)
            table_util.set_table_item_value(invoice_table, i, 5, invoice.drawer)
            table_util.set_table_item_value(invoice_table, i, 6, invoice.beneficiary)
            table_util.set_table_item_value(invoice_table, i, 7, invoice.reviewer)
            table_util.set_table_item_value(invoice_table, i, 8, invoice.start_time)
            table_util.set_table_item_value(invoice_table, i, 9, invoice.total_not_tax)
            table_util.set_table_item_value(invoice_table, i, 10, invoice.total_tax)
            table_util.set_table_item_value(invoice_table, i, 11, invoice.remark)
            table_util.set_table_item_value(invoice_table, i, 15, invoice.serial_number)

            try:
                if invoice.custom:
                    table_util.set_table_item_value(invoice_table, i, 3, invoice.custom.name)
                    table_util.set_table_item_value(invoice_table, i, 12, invoice.custom.code)
                    table_util.set_table_item_value(invoice_table, i, 13, invoice.custom.tax_id)
                    table_util.set_table_item_value(invoice_table, i, 14, invoice.custom.addr)
                    table_util.set_table_item_value(invoice_table, i, 15, invoice.custom.bank_account)
            except Exception:
                pass

    def ok_invoice_export_btn_clicked(self):
        file_name_qstr = QtGui.QFileDialog.getSaveFileName(None, 'Excel', '../', 'Excel File (*.xlsx)')

        if not file_name_qstr:
            return

        file_name = str(file_name_qstr)
        if not file_name.endswith('.xlsx'):
            file_name += '.xlsx'

        invoice_list = list(Invoice.select().where(Invoice.status == 1))
        zuofei_invoice_list = list(Invoice.select().where(Invoice.status == 0))

        elxs_exporter = InvoiceElsxExporter(file_name)
        elxs_exporter.add_invoice_sheet(u"已开发票", invoice_list)
        elxs_exporter.add_invoice_sheet(u"作废发票", zuofei_invoice_list)
        elxs_exporter.close()
        self.show_msg_at_rigth_label(u"导出成功，文件路径：" + file_name)

    def invoice_update_btn_clicked(self):
        table = self.invoice_table
        selected_rows = table_util.get_selected_row_number_list(table)

        if len(selected_rows) != 1:
            QMessageBox.information(self.parentWidget(), "Information", u'请选择一条数据进行修改！')
            return

        id = table_util.str_to_unicode_str(table.item(selected_rows[0], 0).text())
        dialog = InvoiceDialog(self, id)
        dialog.show()

    def invoice_add_btn_clicked(self):
        dialog = InvoiceDialog(self)
        dialog.show()

    def invoice_delete_btn_clicked(self):
        reply = QMessageBox.question(self.parentWidget(), u'提示', u'确定要删除所选记录吗？', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            invoice_table = self.invoice_table

            # 获取所有需要删除的行的ID
            id_list = []
            remove_rows = table_util.get_selected_row_number_list(invoice_table)
            for row_count in remove_rows:
                invoice_id = table_util.str_to_unicode_str(invoice_table.item(row_count, 0).text())
                id_list.append(invoice_id)

            # 删除数据
            q = Invoice.update(status=-1).where(Invoice.id << id_list)
            q.execute()

            # 重新加载表格
            self.invoice_filter_btn_clicked()

    def invoice_import_xml_btn_clicked(self):
        invoice_list = list(Invoice.select(Invoice.status == 0))
        print invoice_list
        is_success = invoice_exporter.export_as_file(invoice_list, "1.xml")
        if is_success:
            QMessageBox.information(self.parentWidget(), "Information", u'导入成功！')
        else:
            QMessageBox.information(self.parentWidget(), "Information", u'导入失败，请重试！')

    def invoice_table_item_clicked(self, item):
        invoice_detail_table = self.invoice_detail_table
        invoice_table = self.invoice_table
        self.show_invoice_detail_in_table(item, invoice_table, invoice_detail_table)

    def ok_invoice_table_item_clicked(self, item):
        invoice_detail_table = self.ok_invoice_detail_table
        invoice_table = self.ok_invoice_table
        self.show_invoice_detail_in_table(item, invoice_table, invoice_detail_table)

    def show_invoice_detail_in_table(self, item, invoice_table, invoice_detail_table):
        # 设置整行选中
        invoice_detail_table.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 设置不可编辑
        invoice_detail_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 获取选中行的ID
        invoice_id = invoice_table.item(item.row(), 0).text()

        # 根据ID查询明细
        invoice_detail_list = list(Invoice.get(id=invoice_id).invoiceDetails)

        row_count = len(invoice_detail_list)
        invoice_detail_table.setRowCount(row_count)

        # 将数据加载到表格中
        for i in range(row_count):
            invoice_detail = invoice_detail_list[i]

            table_util.set_table_item_value(invoice_detail_table, i, 0, invoice_detail.id)
            table_util.set_table_item_value(invoice_detail_table, i, 1, invoice_detail.product.code)
            table_util.set_table_item_value(invoice_detail_table, i, 2, invoice_detail.product.name)
            table_util.set_table_item_value(invoice_detail_table, i, 3, invoice_detail.product.unit_price)
            table_util.set_table_item_value(invoice_detail_table, i, 4, invoice_detail.pro_num)
            table_util.set_table_item_value(invoice_detail_table, i, 5, invoice_detail.contain_tax_price)
            table_util.set_table_item_value(invoice_detail_table, i, 6, invoice_detail.tax_price)
            table_util.set_table_item_value(invoice_detail_table, i, 7, invoice_detail.product.type)
            table_util.set_table_item_value(invoice_detail_table, i, 8, invoice_detail.product.unit)
            table_util.set_table_item_value(invoice_detail_table, i, 9, invoice_detail.product.tax_price)
            table_util.set_table_item_value(invoice_detail_table, i, 10, invoice_detail.not_tax_price)
            table_util.set_table_item_value(invoice_detail_table, i, 11, invoice_detail.product.tax)


    def custom_query_btn_clicked(self):
        custom_table = self.custom_table

        # 设置整行选中
        custom_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置不可编辑
        custom_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 查询数据
        custom_list = list(Custom.select().where(Custom.status == 0))
        row_count = len(custom_list)
        self.custom_table.setRowCount(row_count)

        # 将数据加载到表格中
        for i in range(row_count):
            custom = custom_list[i]
            table_util.set_table_item_value(custom_table, i, 0, custom.id)
            table_util.set_table_item_value(custom_table, i, 1, custom.code)
            table_util.set_table_item_value(custom_table, i, 2, custom.name)
            table_util.set_table_item_value(custom_table, i, 3, custom.tax_id)
            table_util.set_table_item_value(custom_table, i, 4, custom.bank_account)
            table_util.set_table_item_value(custom_table, i, 5, custom.addr)
            table_util.set_table_item_value(custom_table, i, 6, custom.business_tax_id)
            table_util.set_table_item_value(custom_table, i, 7, custom.erp_id)
            table_util.set_table_item_value(custom_table, i, 8, custom.summary_title)
            table_util.set_table_item_value(custom_table, i, 9, custom.remark)

    def custom_update_btn_clicked(self):
        custom_table = self.custom_table
        selected_rows = table_util.get_selected_row_number_list(custom_table)

        if len(selected_rows) != 1:
            QMessageBox.information(self.parentWidget(), "Information", u'请选择一条数据进行修改！')
            return

        invoice_id = table_util.str_to_unicode_str(custom_table.item(selected_rows[0], 0).text())
        dialog = CustomDialog(self, invoice_id)
        dialog.show()

    def custom_add_btn_clicked(self):
        dialog = CustomDialog(self)
        dialog.show()

    def custom_delete_btn_clicked(self):
        reply = QMessageBox.question(self.parentWidget(), u'提示', u'确定要删除所选记录吗？', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            custom_table = self.custom_table
            selected_rows = table_util.get_selected_row_number_list(custom_table)

            # 获取所有需要删除的行的ID
            id_list = []
            for row_count in selected_rows:
                custom_id = table_util.str_to_unicode_str(custom_table.item(row_count, 0).text())
                id_list.append(custom_id)

            # 删除数据
            q = Custom.update(status=1).where(Custom.id << id_list)
            q.execute()

            # 重新加载表格
            self.custom_query_btn_clicked()

    def product_query_btn_clicked(self):
        product_table = self.product_table

        # 设置整行选中
        product_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置不可编辑
        product_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 查询数据
        product_list = list(Product.select().where(Product.status == 0))
        row_count = len(product_list)
        self.product_table.setRowCount(row_count)

        # 将数据加载到表格中
        for i in range(row_count):
            product = product_list[i]
            table_util.set_table_item_value(product_table, i, 0, product.id)
            table_util.set_table_item_value(product_table, i, 1, product.code)
            table_util.set_table_item_value(product_table, i, 2, product.name)
            table_util.set_table_item_value(product_table, i, 3, product.type)
            table_util.set_table_item_value(product_table, i, 4, product.unit)
            table_util.set_table_item_value(product_table, i, 5, product.unit_price)
            table_util.set_table_item_value(product_table, i, 6, product.tax_price)
            table_util.set_table_item_value(product_table, i, 7, product.tax)
            table_util.set_table_item_value(product_table, i, 8, product.business_tax_num)
            table_util.set_table_item_value(product_table, i, 9, product.erp_id)
            table_util.set_table_item_value(product_table, i, 10, product.p_id)

    def product_add_btn_clicked(self):
        dialog = ProductDialog(self)
        dialog.show()

    def product_update_btn_clicked(self):
        product_table = self.product_table
        selected_rows = table_util.get_selected_row_number_list(product_table)

        if len(selected_rows) != 1:
            QMessageBox.information(self.parentWidget().parentWidget(), "Information", u'请选择一条数据进行修改！')
            return

        product_id = table_util.str_to_unicode_str(product_table.item(selected_rows[0], 0).text())
        dialog = ProductDialog(self, product_id)
        dialog.show()

    def product_delete_btn_clicked(self):
        reply = QMessageBox.question(self.parentWidget(), u'提示', u'确定要删除所选记录吗？', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            product_table = self.product_table
            selected_rows = table_util.get_selected_row_number_list(product_table)

            # 获取所有需要删除的行的ID
            id_list = []
            for row_count in selected_rows:
                product_id = table_util.str_to_unicode_str(product_table.item(row_count, 0).text())
                id_list.append(product_id)

            # 删除数据
            q = Product.update(status=1).where(Product.id << id_list)
            q.execute()

            # 重新加载表格
            self.product_query_btn_clicked()

    def section_query_btn_clicked(self):
        table = self.section_table

        # 设置整行选中
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置不可编辑
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 查询数据
        data_list = list(NoSection.select())
        row_count = len(data_list)
        table.setRowCount(row_count)

        # 将数据加载到表格中
        for i in range(row_count):
            no_section = data_list[i]
            table_util.set_table_item_value(table, i, 0, no_section.id)
            table_util.set_table_item_value(table, i, 1, no_section.start_num)
            table_util.set_table_item_value(table, i, 2, no_section.end_num)
            table_util.set_table_item_value(table, i, 3, no_section.user_name)
            table_util.set_table_item_value(table, i, 4, no_section.start_time)
            table_util.set_table_item_value(table, i, 5, no_section.status)

    def section_add_btn_clicked(self):
        dialog = SectionDialog(self)
        dialog.show()

    def section_update_btn_clicked(self):
        table = self.section_table
        selected_rows = table_util.get_selected_row_number_list(table)

        if len(selected_rows) != 1:
            QMessageBox.information(self.parentWidget(), "Information", u'请选择一条数据进行修改！')
            return

        id = table_util.str_to_unicode_str(table.item(selected_rows[0], 0).text())
        dialog = SectionDialog(self, id)
        dialog.show()

    def section_delete_btn_clicked(self):
        reply = QMessageBox.question(self.parentWidget(), u'提示', u'确定要删除所选记录吗？', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            table = self.section_table
            selected_rows = table_util.get_selected_row_number_list(table)

            # 获取所有需要删除的行的ID
            id_list = []
            for row_count in selected_rows:
                id = table_util.str_to_unicode_str(table.item(row_count, 0).text())
                id_list.append(id)

            # 删除数据
            q = NoSection.delete().where(Product.id << id_list)
            q.execute()

            # 重新加载表格
            self.section_query_btn_clicked()

    def user_query_btn_clicked(self):
        table = self.user_table

        # 设置整行选中
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置不可编辑
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 查询数据
        data_list = list(User.select())
        row_count = len(data_list)
        table.setRowCount(row_count)

        # 将数据加载到表格中
        for i in range(row_count):
            user = data_list[i]
            table_util.set_table_item_value(table, i, 0, user.id)
            table_util.set_table_item_value(table, i, 1, user.name)
            table_util.set_table_item_value(table, i, 2, user.login_name)
            if user.is_admin:
                table_util.set_table_item_value(table, i, 3, u"管理员用户")
            else:
                table_util.set_table_item_value(table, i, 3, u"普通用户")

    def user_add_btn_clicked(self):
        dialog = UserDialog(self)
        dialog.show()

    def user_update_btn_clicked(self):
        table = self.user_table
        selected_rows = table_util.get_selected_row_number_list(table)

        if len(selected_rows) != 1:
            QMessageBox.information(self.parentWidget(), "Information", u'请选择一条数据进行修改！')
            return

        id = table_util.str_to_unicode_str(table.item(selected_rows[0], 0).text())
        dialog = UserDialog(self, id)
        dialog.show()

    def user_delete_btn_clicked(self):
        reply = QMessageBox.question(self.parentWidget(), u'提示', u'确定要删除所选记录吗？', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            table = self.user_table
            selected_rows = table_util.get_selected_row_number_list(table)

            # 获取所有需要删除的行的ID
            id_list = []
            for row_count in selected_rows:
                id = table_util.str_to_unicode_str(table.item(row_count, 0).text())
                id_list.append(id)

            # 删除数据
            q = User.delete().where(User.id << id_list)
            q.execute()

            # 重新加载表格
            self.user_query_btn_clicked()