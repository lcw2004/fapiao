# -*- coding: utf-8 -*-

from PyQt4.QtGui import QMainWindow, QMessageBox, QAbstractItemView
from PyQt4 import QtCore
from PyQt4 import QtGui
from invoice.bean.ProductBean import Product
from invoice.dao.ProductDao import ProductDao
from mainwindow_ui import Ui_MainWindow

from invoice.sys import ExportAsXML
from invoice.common import excelparse
from invoice.common import tableUtil
from invoice.bean.InvoiceBean import Invoice
from invoice.bean.InvoiceDetailBean import InvoiceDetail
from invoice.bean.CustomBean import Custom
from invoice.dao.InvoiceDao import InvoiceDao
from invoice.dao.InvoiceDetailDao import InvoiceDetailDao
from invoice.dao.CustomDao import CustomDao

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 绑定选择Excel事件
        self.connect(self.selectExcelFileButton, QtCore.SIGNAL("clicked()"), self.selectExcel)

        # 数据导入 - 生成发票
        self.connect(self.genInvoiceButton, QtCore.SIGNAL("clicked()"), self.genInvoice)

        # 临时待处理数据 - 表格加载
        self.connect(self.invoice_filter_Button, QtCore.SIGNAL("clicked()"), self.queryInvoice)

        # 绑定元素选择事件
        self.connect(self.invoiceTableWidget, QtCore.SIGNAL('itemClicked(QTableWidgetItem*)'), self.invoinceItem_Clicked)

        # 临时待处理数据 - 修改
        self.connect(self.invoince_update_btn, QtCore.SIGNAL("clicked()"), self.updateInvoince)

        # 临时待处理数据 - 删除
        self.connect(self.invoince_delete_btn, QtCore.SIGNAL("clicked()"), self.on_action_Delete_Invoice)

        # 临时待处理数据 - 导入到开票系统
        self.connect(self.invoince_import_xml_btn, QtCore.SIGNAL("clicked()"), self.exportInvoinceAsXml)

        # 临时待处理数据 - 合并选中项
        self.connect(self.invoince_merge_btn, QtCore.SIGNAL("clicked()"), self.mergeInvoice)

        # 临时待处理数据 - 拆分
        self.connect(self.invoince_chaifeng_btn, QtCore.SIGNAL("clicked()"), self.chaifenInvoice)


    def mergeInvoice(self):
        invoiceTableWidget = self.invoiceTableWidget

        # 判断选择的合并的发票数量
        selected_rows = tableUtil.getSelectedRows(invoiceTableWidget)
        if len(selected_rows) <= 1:
            QMessageBox.information(self, "Information", u'请选择至少两个需要合并的发票！')
            return

        # 获取所有需要合并的行的ID
        idList = []
        customNameList = []
        for row_num in selected_rows:
            invoince_id = tableUtil.qStringToString(invoiceTableWidget.item(row_num, 0).text())
            invoince_custom_name = tableUtil.qStringToString(invoiceTableWidget.item(row_num, 2).text())
            if invoince_id:
                idList.append(int(invoince_id))
                customNameList.append(invoince_custom_name)

        # 判断是否
        customNameSet = set(customNameList)
        if len(customNameSet) > 1:
            QMessageBox.information(self, "Information", u'所选发票中存在两个不同客户的发票！')
            return

        # 将所选发票的详细信息合并到第一个中，并删除其他发票
        mainInvoiceId = idList[0]
        invoiceDao = InvoiceDao()
        invoiceDao.mergeInvoinceDetail(mainInvoiceId, idList)
        invoiceDao.updateStatus(idList[1:], 9)

        # 合并成功并刷新表格
        QMessageBox.information(self, "Information", u'合并成功！')
        self.queryInvoice()

    def chaifenInvoice(self):
        pass

    def selectExcel(self):
        # TODO 判断是否选择文件
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Excel', '../', 'Excel File (*.xls)')
        if filename:
            excelparse.parseExcel(filename, self.excelTableWidget)

    def genInvoice(self):
        excelTableWidget = self.excelTableWidget
        rowCount = excelTableWidget.rowCount()
        colCount = excelTableWidget.columnCount()

        # TODO 判断表格中是否有数据
        if rowCount <= 1:
            QMessageBox.information(self, "Information", u'请先导入发票数据！')
            return

        invoiceDao = InvoiceDao()
        invoiceDetailDao = InvoiceDetailDao()
        cuntomDao = CustomDao()
        productDao = ProductDao()

        for i in range(rowCount):
            tbl_custom_name = tableUtil.qStringToString(excelTableWidget.item(i, 0).text())
            tbl_invoice_invoice_num = tableUtil.qStringToString(excelTableWidget.item(i, 1).text())
            tbl_invoice_total_not_tax = tableUtil.qStringToString(excelTableWidget.item(i, 2).text())
            tbl_invoice_detail_pro_type = tableUtil.qStringToString(excelTableWidget.item(i, 3).text())
            tbl_invoice_detail_pro_name = tableUtil.qStringToString(excelTableWidget.item(i, 4).text())
            tbl_invoice_remark = tableUtil.qStringToString(excelTableWidget.item(i, 5).text())

            # 保存用户信息
            custom = cuntomDao.getOne(name=tbl_custom_name)
            if custom:
                print u"客户已经存在，ID为：", custom.id
            else:
                custom = Custom()
                custom.name = tbl_custom_name
                custom.id = cuntomDao.save(custom)

            # 保存商品信息
            product = productDao.getOne(name=tbl_invoice_detail_pro_name)
            if product:
                print u"商品已经存在，ID为：", product.id
            else:
                product = Product()
                product.name = tbl_invoice_detail_pro_name
                product.type = tbl_invoice_detail_pro_type
                product.id = productDao.save(product)

            # 保存发票
            invoice = Invoice()
            invoice.invoice_num = tbl_invoice_invoice_num
            invoice.remark = tbl_invoice_remark
            invoice.total_not_tax = tbl_invoice_total_not_tax
            invoice.custom_id = custom.id
            invoice.id = invoiceDao.save(invoice)

            # 保存发票详细信息
            invoiceDetail = InvoiceDetail()
            invoiceDetail.pro_type = tbl_invoice_detail_pro_type
            invoiceDetail.pro_name = tbl_invoice_detail_pro_name
            invoiceDetail.invoice_Id = invoice.id
            invoiceDetail.product_id = product.id
            invoiceDetailDao.save(invoiceDetail)

            print tbl_invoice_invoice_num
            print tbl_invoice_total_not_tax
            print tbl_invoice_detail_pro_type
            print tbl_invoice_detail_pro_name
            print tbl_invoice_remark
            print "-------------------------------"

        QMessageBox.information(self, "Information", u'数据已经保存到临时数据区！')

    def queryInvoice(self):
        invoiceTableWidget = self.invoiceTableWidget

        # 设置整行选中
        invoiceTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置不可编辑
        invoiceTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 查询数据
        invoiceDao = InvoiceDao()
        invoiceList = invoiceDao.getAllData(0)

        # 将数据填充到表格中
        invoiceCount = len(invoiceList)
        self.invoiceTableWidget.setRowCount(invoiceCount)
        for i in range(invoiceCount):
            invoice = invoiceList[i]
            tableUtil.setTableItemValue(invoiceTableWidget, i, 0, invoice.id)
            tableUtil.setTableItemValue(invoiceTableWidget, i, 1, invoice.invoice_num)
            if invoice.custom:
                tableUtil.setTableItemValue(invoiceTableWidget, i, 2, invoice.custom.name)
                tableUtil.setTableItemValue(invoiceTableWidget, i, 7, invoice.custom.code)
                tableUtil.setTableItemValue(invoiceTableWidget, i, 8, invoice.custom.tax_id)
                tableUtil.setTableItemValue(invoiceTableWidget, i, 9, invoice.custom.addr)
                tableUtil.setTableItemValue(invoiceTableWidget, i, 10, invoice.custom.bank_account)

            tableUtil.setTableItemValue(invoiceTableWidget, i, 3, invoice.total_not_tax)
            tableUtil.setTableItemValue(invoiceTableWidget, i, 4, invoice.total_tax)
            tableUtil.setTableItemValue(invoiceTableWidget, i, 5, invoice.total_num)
            tableUtil.setTableItemValue(invoiceTableWidget, i, 6, invoice.serial_number)

            tableUtil.setTableItemValue(invoiceTableWidget, i, 11, invoice.remark)
            tableUtil.setTableItemValue(invoiceTableWidget, i, 12, invoice.drawer)
            tableUtil.setTableItemValue(invoiceTableWidget, i, 13, invoice.beneficiary)
            tableUtil.setTableItemValue(invoiceTableWidget, i, 14, invoice.reviewer)


    def updateInvoince(self):
        pass

    def on_action_Delete_Invoice(self):
            reply = QMessageBox.question(self,u'提示',u'确定要删除所选记录吗？',QMessageBox.Yes|QMessageBox.No)
            if reply == QMessageBox.Yes:
                invoiceTableWidget = self.invoiceTableWidget

                # 获取所有需要删除的行的ID
                idList = []
                remove_rows = tableUtil.getSelectedRows(invoiceTableWidget)
                for rowCount in remove_rows:
                    invoince_id = tableUtil.qStringToString(invoiceTableWidget.item(rowCount, 0).text())
                    if invoince_id:
                        idList.append(int(invoince_id))

                # 删除数据库中的数据
                invoiceDao = InvoiceDao()
                invoiceDao.updateStatus(idList, -1)

                # 重新加载表格
                self.queryInvoice(self)

    def exportInvoinceAsXml(self):
        invoiceDao = InvoiceDao()
        invoinceList = invoiceDao.getAllData(0)
        isSuccess =  ExportAsXML.exportAsFile(invoinceList, "1.xml")
        if isSuccess:
            QMessageBox.information(self, "Information", u'导入成功！')
        else:
            QMessageBox.information(self, "Information", u'导入失败，请重试！')

    def invoinceItem_Clicked(self, item):
        # 获取选中行的ID
        invoiceId =  self.invoiceTableWidget.item(item.row(), 0).text()

        # 根据ID查询明细
        invoiceDetailDao = InvoiceDetailDao()
        invoiceDetailList = invoiceDetailDao.get(invoiceId)
        invoiceDetailCount = len(invoiceDetailList)

        # 将数据加载到表格中
        invoinceDetailTableWidget = self.invoinceDetailTableWidget
        invoinceDetailTableWidget.setRowCount(invoiceDetailCount)
        for i in range(invoiceDetailCount):
            invoiceDetail = invoiceDetailList[i]

            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 0, invoiceDetail.id)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 1, invoiceDetail.pro_code)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 2, invoiceDetail.pro_name)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 3, invoiceDetail.pro_type)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 4, invoiceDetail.pro_unit)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 5, invoiceDetail.pro_unit_price)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 6, invoiceDetail.pro_num)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 7, invoiceDetail.tax_price)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 8, invoiceDetail.tax_rate)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 9, invoiceDetail.tax)



