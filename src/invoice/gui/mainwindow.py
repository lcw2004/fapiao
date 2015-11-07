# -*- coding: utf-8 -*-
import logging

from PyQt4.QtGui import QMainWindow, QMessageBox, QAbstractItemView
from PyQt4 import QtCore
from PyQt4 import QtGui
from invoice.gui.form_custom import CustomDialog

from mainwindow_ui import Ui_MainWindow
from invoice.sys import invoice_exporter
from invoice.common import excel_parser
from invoice.common import table_util
from invoice.bean.beans import *

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 绑定选择Excel事件
        self.connect(self.excel_selectl_file_btn, QtCore.SIGNAL("clicked()"), self.excel_select_file_btn_clicked)

        # 数据导入 - 生成发票
        self.connect(self.excel_gen_invoice_btn, QtCore.SIGNAL("clicked()"), self.excel_gen_invoice_btn_clicked)

        # 临时待处理数据 - 表格加载
        self.connect(self.invoice_filter_btn, QtCore.SIGNAL("clicked()"), self.invoice_filter_btn_clicked)

        # 绑定元素选择事件
        self.connect(self.invoice_table, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'),
                     self.invoice_table_item_clicked)

        # 临时待处理数据 - 修改
        self.connect(self.invoine_update_btn, QtCore.SIGNAL("clicked()"), self.invoice_update_btn_clicked)

        # 临时待处理数据 - 删除
        self.connect(self.invoice_delete_btn, QtCore.SIGNAL("clicked()"), self.invoice_delete_btn_clicked)

        # 临时待处理数据 - 导入到开票系统
        self.connect(self.invoice_import_xml_btn, QtCore.SIGNAL("clicked()"), self.invoice_import_xml_btn_clicked)

        # 临时待处理数据 - 合并选中项
        self.connect(self.invoice_merge_btn, QtCore.SIGNAL("clicked()"), self.invoice_merge_btn_clicked)

        # 临时待处理数据 - 合并发票相同的产品
        self.connect(self.invoice_merge_product_btn, QtCore.SIGNAL("clicked()"), self.invoice_merge_product_btn_clicked)

        # 临时待处理数据 - 拆分(按最大限额)
        self.connect(self.invoice_chaifeng_btn, QtCore.SIGNAL("clicked()"), self.invoice_chaifeng_btn_clicked)

        ###############
        ## 客户管理模块
        self.connect(self.custom_query_btn, QtCore.SIGNAL("clicked()"), self.custom_query_btn_clicked)
        self.connect(self.custom_add_btn, QtCore.SIGNAL("clicked()"), self.custom_add_btn_clicked)
        self.connect(self.custom_update_btn, QtCore.SIGNAL("clicked()"), self.custom_update_btn_clicked)
        self.connect(self.custom_delete_btn, QtCore.SIGNAL("clicked()"), self.custom_delete_btn_clicked)
        ###############

        ###############
        ## 产品管理模块
        self.connect(self.product_query_btn, QtCore.SIGNAL("clicked()"), self.product_query_btn_clicked)

        ###############

    def invoice_merge_product_btn_clicked(self):
        pass

    def invoice_merge_btn_clicked(self):
        invoice_table = self.invoice_table

        # 判断选择的合并的发票数量
        selected_rows = table_util.get_selected_row_number_list(invoice_table)
        if len(selected_rows) <= 1:
            QMessageBox.information(None, "Information", u'请选择至少两个需要合并的发票！')
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
        customNameSet = set(custom_name_list)
        if len(customNameSet) > 1:
            QMessageBox.information(None, "Information", u'所选发票中存在两个不同客户的发票！')
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
        QMessageBox.information(None, "Information", u'合并成功！')
        self.invoice_filter_btn_clicked()

    def invoice_chaifeng_btn_clicked(self):
        invoice_detail_table = self.invoice_detail_table

        # 判断选择的合并的发票数量
        selected_rows = table_util.get_selected_row_number_list(invoice_detail_table)
        if len(selected_rows) < 1:
            QMessageBox.information(None, "Information", u'请选择至少一个需要拆分的发票明细！')
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
            QMessageBox.information(None, "Information", u'拆分成功！')
            self.invoice_filter_btn_clicked()

        pass

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
        row_count = excel_table.rowCount()
        col_count = excel_table.columnCount()

        # TODO 判断表格中是否有数据
        if row_count <= 1:
            QMessageBox.information(None, "Information", u'请先导入发票数据！')
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
            invoiceDetail_of_this = InvoiceDetail.create(
                pro_type=tbl_invoice_detail_pro_type,
                pro_name=tbl_invoice_detail_pro_name,
                not_tax_price=tbl_invoice_total_not_tax,
                invoice_Id=invoice_of_this.id,
                product_id=product_of_this.id,
                invoice=invoice_of_this,
                product=product_of_this
            )
            invoiceDetail_of_this.save()

            # TODO 计算税额
            # invoiceDetail.caculate()
            # invoiceDao.proofreadInvoince(invoice.id)

        QMessageBox.information(None, "Information", u'数据已经保存到临时数据区！')
        # TODO 导入成功之后清空数据

    def invoice_filter_btn_clicked(self):
        invoice_table = self.invoice_table

        # 设置整行选中
        invoice_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置不可编辑
        invoice_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 查询数据
        invoice_list = list(Invoice.select().where(Invoice.status == 0))

        rowCount = len(invoice_list)
        self.invoice_table.setRowCount(rowCount)

        # 将数据加载到表格中
        for i in range(rowCount):
            invoice = invoice_list[i]

            table_util.set_table_item_value(invoice_table, i, 0, invoice.id)
            table_util.set_table_item_value(invoice_table, i, 1, invoice.invoice_num)
            if invoice.custom:
                table_util.set_table_item_value(invoice_table, i, 2, invoice.custom.name)
                table_util.set_table_item_value(invoice_table, i, 7, invoice.custom.code)
                table_util.set_table_item_value(invoice_table, i, 8, invoice.custom.tax_id)
                table_util.set_table_item_value(invoice_table, i, 9, invoice.custom.addr)
                table_util.set_table_item_value(invoice_table, i, 10, invoice.custom.bank_account)

            table_util.set_table_item_value(invoice_table, i, 3, invoice.total_not_tax)
            table_util.set_table_item_value(invoice_table, i, 4, invoice.total_tax)
            table_util.set_table_item_value(invoice_table, i, 5, invoice.total_num)
            table_util.set_table_item_value(invoice_table, i, 6, invoice.serial_number)

            table_util.set_table_item_value(invoice_table, i, 11, invoice.remark)
            table_util.set_table_item_value(invoice_table, i, 12, invoice.drawer)
            table_util.set_table_item_value(invoice_table, i, 13, invoice.beneficiary)
            table_util.set_table_item_value(invoice_table, i, 14, invoice.reviewer)

    def invoice_update_btn_clicked(self):
        # dialog = FormInvoiceDialog(self)
        # dialog.show()
        pass

    def invoice_delete_btn_clicked(self):
        reply = QMessageBox.question(self, u'提示', u'确定要删除所选记录吗？', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            invoice_table = self.invoice_table

            # 获取所有需要删除的行的ID
            idList = []
            remove_rows = table_util.get_selected_row_number_list(invoice_table)
            for rowCount in remove_rows:
                invoice_id = table_util.str_to_unicode_str(invoice_table.item(rowCount, 0).text())
                idList.append(invoice_id)

            # 删除数据
            q = Invoice.update(status=-1).where(Invoice.id << idList)
            q.execute()

            # 重新加载表格
            self.invoice_filter_btn_clicked()

    def invoice_import_xml_btn_clicked(self):
        invoiceList = list(Invoice.select(Invoice.status == 0))
        print invoiceList
        isSuccess = invoice_exporter.export_as_file(invoiceList, "1.xml")
        if isSuccess:
            QMessageBox.information(None, "Information", u'导入成功！')
        else:
            QMessageBox.information(None, "Information", u'导入失败，请重试！')

    def invoice_table_item_clicked(self, item):
        invoice_detail_table = self.invoice_detail_table

        # 设置整行选中
        invoice_detail_table.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 设置不可编辑
        invoice_detail_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 获取选中行的ID
        invoiceId = self.invoice_table.item(item.row(), 0).text()

        # 根据ID查询明细
        invoiceDetailList = list(Invoice.get(id=invoiceId).invoiceDetails)

        rowCount = len(invoiceDetailList)
        self.invoice_detail_table.setRowCount(rowCount)

        # 将数据加载到表格中
        for i in range(rowCount):
            invoiceDetail = invoiceDetailList[i]

            table_util.set_table_item_value(invoice_detail_table, i, 0, invoiceDetail.id)
            table_util.set_table_item_value(invoice_detail_table, i, 1, invoiceDetail.product.code)
            table_util.set_table_item_value(invoice_detail_table, i, 2, invoiceDetail.product.name)
            table_util.set_table_item_value(invoice_detail_table, i, 3, invoiceDetail.product.type)
            table_util.set_table_item_value(invoice_detail_table, i, 4, invoiceDetail.product.unit)
            table_util.set_table_item_value(invoice_detail_table, i, 5, invoiceDetail.product.unit_price)
            table_util.set_table_item_value(invoice_detail_table, i, 6, invoiceDetail.pro_num)
            table_util.set_table_item_value(invoice_detail_table, i, 7, invoiceDetail.product.tax_price)
            table_util.set_table_item_value(invoice_detail_table, i, 8, invoiceDetail.not_tax_price)
            table_util.set_table_item_value(invoice_detail_table, i, 9, invoiceDetail.product.tax)
            table_util.set_table_item_value(invoice_detail_table, i, 10, invoiceDetail.tax_price)
            table_util.set_table_item_value(invoice_detail_table, i, 11, invoiceDetail.contain_tax_price)

    def custom_query_btn_clicked(self):
        custom_table = self.custom_table

        # 设置整行选中
        custom_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置不可编辑
        custom_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 查询数据
        custom_list = list(Custom.select().where(Custom.status==0))
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
            QMessageBox.information(None, "Information", u'请选择一条数据进行修改！')
            return

        invoice_id = table_util.str_to_unicode_str(custom_table.item(selected_rows[0], 0).text())
        dialog = CustomDialog(self, invoice_id)
        dialog.show()

    def custom_add_btn_clicked(self):
        dialog = CustomDialog(self)
        dialog.show()

    def custom_delete_btn_clicked(self):
        reply = QMessageBox.question(self, u'提示', u'确定要删除所选记录吗？', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            custom_table = self.custom_table
            selected_rows = table_util.get_selected_row_number_list(custom_table)

            # 获取所有需要删除的行的ID
            id_list = []
            for rowCount in selected_rows:
                id = table_util.str_to_unicode_str(custom_table.item(rowCount, 0).text())
                id_list.append(id)

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
        product_list = list(Product.select())
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
            table_util.set_table_item_value(product_table, i, 9, product.p_id)
