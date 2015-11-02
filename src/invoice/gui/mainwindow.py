# -*- coding: utf-8 -*-

from PyQt4.QtGui import QMainWindow, QMessageBox, QAbstractItemView
from PyQt4 import QtCore
from PyQt4 import QtGui

from mainwindow_ui import Ui_MainWindow
from invoice.sys import ExportAsXML
from invoice.common import excelparse
from invoice.common import tableUtil
from invoice.bean.Beans import *


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 绑定选择Excel事件
        self.connect(self.excel_selectl_file_btn, QtCore.SIGNAL("clicked()"), self.excel_selectl_file_btn_clicked)

        # 数据导入 - 生成发票
        self.connect(self.excel_gen_invoice_btn, QtCore.SIGNAL("clicked()"), self.excel_gen_invoice_btn_clicked)

        # 临时待处理数据 - 表格加载
        self.connect(self.invoice_filter_btn, QtCore.SIGNAL("clicked()"), self.invoice_filter_btn_clicked)

        # 绑定元素选择事件
        self.connect(self.invoice_table, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.invoice_table_item_clicked)

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
        selected_rows = tableUtil.getSelectedRows(invoice_table)
        if len(selected_rows) <= 1:
            QMessageBox.information(None, "Information", u'请选择至少两个需要合并的发票！')
            return

        # 获取所有需要合并的行的ID
        invoice_id_list = []
        custom_name_list = []
        for row_num in selected_rows:
            invoice_id = tableUtil.qStringToString(invoice_table.item(row_num, 0).text())
            invoice_custom_name = tableUtil.qStringToString(invoice_table.item(row_num, 2).text())
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
        selected_rows = tableUtil.getSelectedRows(invoice_detail_table)
        if len(selected_rows) < 1:
            QMessageBox.information(None, "Information", u'请选择至少一个需要拆分的发票明细！')
            return

        # 获取所有需要合并的行的ID
        invoice_id_list = []
        for row_num in selected_rows:
            invoice_id = tableUtil.qStringToString(invoice_detail_table.item(row_num, 0).text())
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

    def excel_selectl_file_btn_clicked(self):
        # TODO 判断是否选择文件
        filename = QtGui.QFileDialog.getOpenFileName(None, 'Excel', '../', 'Excel File (*.xls)')
        if filename:
            excelparse.parseExcel(filename, self.excel_table)

    def excel_gen_invoice_btn_clicked(self):
        excel_table = self.excel_table
        row_count = excel_table.rowCount()
        col_count = excel_table.columnCount()

        # TODO 判断表格中是否有数据
        if row_count <= 1:
            QMessageBox.information(None, "Information", u'请先导入发票数据！')
            return

        for i in range(row_count):
            tbl_custom_name = tableUtil.qStringToString(excel_table.item(i, 0).text())
            tbl_invoice_invoice_num = tableUtil.qStringToString(excel_table.item(i, 1).text())
            tbl_invoice_total_not_tax = tableUtil.qStringToString(excel_table.item(i, 2).text())
            tbl_invoice_detail_pro_type = tableUtil.qStringToString(excel_table.item(i, 3).text())
            tbl_invoice_detail_pro_name = tableUtil.qStringToString(excel_table.item(i, 4).text())
            tbl_invoice_remark = tableUtil.qStringToString(excel_table.item(i, 5).text())

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

            print tbl_invoice_invoice_num
            print tbl_invoice_total_not_tax
            print tbl_invoice_detail_pro_type
            print tbl_invoice_detail_pro_name
            print tbl_invoice_remark
            print "-------------------------------"

        QMessageBox.information(None, "Information", u'数据已经保存到临时数据区！')
        # TODO 导入成功之后清空数据

    def invoice_filter_btn_clicked(self):
        invoice_table = self.invoice_table

        # 设置整行选中
        invoice_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置不可编辑
        invoice_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 查询数据
        invoice_list = list(Invoice.select().where(Invoice.status==0))


        rowCount = len(invoice_list)
        self.invoice_table.setRowCount(rowCount)

        # 将数据加载到表格中
        for i in range(rowCount):
            invoice = invoice_list[i]

            tableUtil.setTableItemValue(invoice_table, i, 0, invoice.id)
            tableUtil.setTableItemValue(invoice_table, i, 1, invoice.invoice_num)
            if invoice.custom:
                tableUtil.setTableItemValue(invoice_table, i, 2, invoice.custom.name)
                tableUtil.setTableItemValue(invoice_table, i, 7, invoice.custom.code)
                tableUtil.setTableItemValue(invoice_table, i, 8, invoice.custom.tax_id)
                tableUtil.setTableItemValue(invoice_table, i, 9, invoice.custom.addr)
                tableUtil.setTableItemValue(invoice_table, i, 10, invoice.custom.bank_account)

            tableUtil.setTableItemValue(invoice_table, i, 3, invoice.total_not_tax)
            tableUtil.setTableItemValue(invoice_table, i, 4, invoice.total_tax)
            tableUtil.setTableItemValue(invoice_table, i, 5, invoice.total_num)
            tableUtil.setTableItemValue(invoice_table, i, 6, invoice.serial_number)

            tableUtil.setTableItemValue(invoice_table, i, 11, invoice.remark)
            tableUtil.setTableItemValue(invoice_table, i, 12, invoice.drawer)
            tableUtil.setTableItemValue(invoice_table, i, 13, invoice.beneficiary)
            tableUtil.setTableItemValue(invoice_table, i, 14, invoice.reviewer)

    def invoice_update_btn_clicked(self):
        # dialog = FormInvoiceDialog(self)
        # dialog.show()
        pass

    def invoice_delete_btn_clicked(self):
            reply = QMessageBox.question(self,u'提示',u'确定要删除所选记录吗？',QMessageBox.Yes|QMessageBox.No)
            if reply == QMessageBox.Yes:
                invoice_table = self.invoice_table

                # 获取所有需要删除的行的ID
                idList = []
                remove_rows = tableUtil.getSelectedRows(invoice_table)
                for rowCount in remove_rows:
                    invoice_id = tableUtil.qStringToString(invoice_table.item(rowCount, 0).text())
                    if invoice_id:
                        q = Invoice.update(status=-1).where(Invoice.id == invoice_id)
                        q.execute()

                # 重新加载表格
                self.invoice_filter_btn_clicked()

    def invoice_import_xml_btn_clicked(self):
        invoiceList = list(Invoice.select(Invoice.status == 0))
        print invoiceList
        isSuccess = ExportAsXML.exportAsFile(invoiceList, "1.xml")
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
        invoiceId =  self.invoice_table.item(item.row(), 0).text()

        # 根据ID查询明细
        invoiceDetailList = list(Invoice.get(id=invoiceId).invoiceDetails)

        rowCount = len(invoiceDetailList)
        self.invoice_detail_table.setRowCount(rowCount)

        # 将数据加载到表格中
        for i in range(rowCount):
            invoiceDetail = invoiceDetailList[i]

            tableUtil.setTableItemValue(invoice_detail_table, i, 0, invoiceDetail.id)
            tableUtil.setTableItemValue(invoice_detail_table, i, 1, invoiceDetail.product.code)
            tableUtil.setTableItemValue(invoice_detail_table, i, 2, invoiceDetail.product.name)
            tableUtil.setTableItemValue(invoice_detail_table, i, 3, invoiceDetail.product.type)
            tableUtil.setTableItemValue(invoice_detail_table, i, 4, invoiceDetail.product.unit)
            tableUtil.setTableItemValue(invoice_detail_table, i, 5, invoiceDetail.product.unit_price)
            tableUtil.setTableItemValue(invoice_detail_table, i, 6, invoiceDetail.pro_num)
            tableUtil.setTableItemValue(invoice_detail_table, i, 7, invoiceDetail.product.tax_price)
            tableUtil.setTableItemValue(invoice_detail_table, i, 8, invoiceDetail.not_tax_price)
            tableUtil.setTableItemValue(invoice_detail_table, i, 9, invoiceDetail.product.tax)
            tableUtil.setTableItemValue(invoice_detail_table, i, 10, invoiceDetail.tax_price)
            tableUtil.setTableItemValue(invoice_detail_table, i, 11, invoiceDetail.contain_tax_price)

    def custom_query_btn_clicked(self):
        custom_table = self.custom_table

        # 设置整行选中
        custom_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置不可编辑
        custom_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 查询数据
        custom_list = list(Custom.select())
        row_count = len(custom_list)
        self.custom_table.setRowCount(row_count)

        # 将数据加载到表格中
        for i in range(row_count):
            custom = custom_list[i]
            tableUtil.setTableItemValue(custom_table, i, 0, custom.id)
            tableUtil.setTableItemValue(custom_table, i, 1, custom.code)
            tableUtil.setTableItemValue(custom_table, i, 2, custom.name)
            tableUtil.setTableItemValue(custom_table, i, 3, custom.tax_id)
            tableUtil.setTableItemValue(custom_table, i, 4, custom.bank_account)
            tableUtil.setTableItemValue(custom_table, i, 5, custom.addr)
            tableUtil.setTableItemValue(custom_table, i, 6, custom.business_tax_di)
            tableUtil.setTableItemValue(custom_table, i, 7, custom.erp_id)
            tableUtil.setTableItemValue(custom_table, i, 8, custom.summary_title)

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
            tableUtil.setTableItemValue(product_table, i, 0, product.id)
            tableUtil.setTableItemValue(product_table, i, 1, product.code)
            tableUtil.setTableItemValue(product_table, i, 2, product.name)
            tableUtil.setTableItemValue(product_table, i, 3, product.type)
            tableUtil.setTableItemValue(product_table, i, 4, product.unit)
            tableUtil.setTableItemValue(product_table, i, 5, product.unit_price)
            tableUtil.setTableItemValue(product_table, i, 6, product.tax_price)
            tableUtil.setTableItemValue(product_table, i, 7, product.tax)
            tableUtil.setTableItemValue(product_table, i, 8, product.business_tax_num)
            tableUtil.setTableItemValue(product_table, i, 9, product.p_id)
