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

        # 临时待处理数据 - 合并发票相同的产品
        self.connect(self.invoince_merge_product_btn, QtCore.SIGNAL("clicked()"), self.mergeInvoiceDetail)

        # 临时待处理数据 - 拆分(按最大限额)
        self.connect(self.invoince_chaifeng_btn, QtCore.SIGNAL("clicked()"), self.chaifenInvoice)

    def mergeInvoiceDetail(self):
        invoiceTableWidget = self.invoiceTableWidget

        rowCount = invoiceTableWidget.rowCount()


        # 获取所有需要合并的行的ID
        idList = []
        for row_num in range(rowCount):
            invoince_id = tableUtil.qStringToString(invoiceTableWidget.item(row_num, 0).text())
            if invoince_id:
                invoiceDetailDao = InvoiceDetailDao()
                invoiceDetailList = invoiceDetailDao.queryChongFu(invoince_id)
                for invoiceDetail in invoiceDetailList:
                    print "------------------------"
                    print invoiceDetail.id
                    print invoiceDetail.pro_num
                    print invoiceDetail.not_tax_price
                    print invoiceDetail.tax_price
                    print invoiceDetail.contain_tax_price
                    print invoiceDetail.invoice_Id
                    print invoiceDetail.product_id


        # 重新统计税额
        # invoiceDao.proofreadInvoince(mainInvoiceId)

        # 合并成功并刷新表格
        QMessageBox.information(self, "Information", u'合并成功！')
        self.queryInvoice()

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

        # 重新统计税额
        invoiceDao.proofreadInvoince(mainInvoiceId)

        # 合并成功并刷新表格
        QMessageBox.information(self, "Information", u'合并成功！')
        self.queryInvoice()


    def chaifenInvoice(self):
        invoinceDetailTableWidget = self.invoinceDetailTableWidget

        # 判断选择的合并的发票数量
        selected_rows = tableUtil.getSelectedRows(invoinceDetailTableWidget)
        if len(selected_rows) < 1:
            QMessageBox.information(self, "Information", u'请选择至少一个需要拆分的发票明细！')
            return

        # 获取所有需要合并的行的ID
        idList = []
        for row_num in selected_rows:
            invoince_id = tableUtil.qStringToString(invoinceDetailTableWidget.item(row_num, 0).text())
            if invoince_id:
                idList.append(int(invoince_id))

        # 获取发票ID
        invoiceDetailDao = InvoiceDetailDao()
        invoiceDao = InvoiceDao()
        if idList:
            invoiceDetail = invoiceDetailDao.getById(idList[0])
            oldInvoiceId = invoiceDetail.invoice_Id
            invoice = invoiceDao.getById(oldInvoiceId)
            newInvoiceId = invoiceDao.save(invoice)
            invoiceDetailDao.updateInvoiceId(idList, newInvoiceId)

            # 重新统计税额
            invoiceDao.proofreadInvoince(newInvoiceId)
            invoiceDao.proofreadInvoince(oldInvoiceId)
            QMessageBox.information(self, "Information", u'拆分成功！')
            self.queryInvoice()

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

        for i in range(rowCount):
            tbl_custom_name = tableUtil.qStringToString(excelTableWidget.item(i, 0).text())
            tbl_invoice_invoice_num = tableUtil.qStringToString(excelTableWidget.item(i, 1).text())
            tbl_invoice_total_not_tax = tableUtil.qStringToString(excelTableWidget.item(i, 2).text())
            tbl_invoice_detail_pro_type = tableUtil.qStringToString(excelTableWidget.item(i, 3).text())
            tbl_invoice_detail_pro_name = tableUtil.qStringToString(excelTableWidget.item(i, 4).text())
            tbl_invoice_remark = tableUtil.qStringToString(excelTableWidget.item(i, 5).text())

            # 保存用户信息
            custom_of_this = Custom.get(name=tbl_custom_name)
            if custom_of_this:
                print u"客户已经存在，ID为：", custom_of_this.id
            else:
                custom_of_this = Custom.create(name=tbl_custom_name)
                custom_of_this.save()

            # 保存商品信息
            product_of_this = Product.get(name=tbl_invoice_detail_pro_name)
            if product_of_this:
                print u"商品已经存在，ID为：", product_of_this.id
            else:
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

        QMessageBox.information(self, "Information", u'数据已经保存到临时数据区！')

    def queryInvoice(self):
        invoiceTableWidget = self.invoiceTableWidget

        # 设置整行选中
        invoiceTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置不可编辑
        invoiceTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 查询数据
        invoiceList = list(Invoice.select().where(Invoice.status==0))


        rowCount = len(invoiceList)
        self.invoiceTableWidget.setRowCount(rowCount)

        # 将数据加载到表格中
        for i in range(rowCount):
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
                        q = Invoice.update(status=-1).where(Invoice.id == invoince_id)
                        q.execute()

                # 重新加载表格
                self.queryInvoice()

    def exportInvoinceAsXml(self):
        invoinceList = list(Invoice.select(Invoice.status == 0))
        isSuccess = ExportAsXML.exportAsFile(invoinceList, "1.xml")
        if isSuccess:
            QMessageBox.information(self, "Information", u'导入成功！')
        else:
            QMessageBox.information(self, "Information", u'导入失败，请重试！')

    def invoinceItem_Clicked(self, item):
        invoinceDetailTableWidget = self.invoinceDetailTableWidget

        # 设置整行选中
        invoinceDetailTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 设置不可编辑
        invoinceDetailTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 获取选中行的ID
        invoiceId =  self.invoiceTableWidget.item(item.row(), 0).text()

        # 根据ID查询明细
        invoiceDetailList = list(Invoice.get(id=invoiceId).invoiceDetails)

        rowCount = len(invoiceDetailList)
        self.invoinceDetailTableWidget.setRowCount(rowCount)

        # 将数据加载到表格中
        for i in range(rowCount):
            invoiceDetail = invoiceDetailList[i]

            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 0, invoiceDetail.id)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 1, invoiceDetail.product.code)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 2, invoiceDetail.product.name)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 3, invoiceDetail.product.type)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 4, invoiceDetail.product.unit)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 5, invoiceDetail.product.unit_price)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 6, invoiceDetail.pro_num)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 7, invoiceDetail.product.tax_price)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 8, invoiceDetail.not_tax_price)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 9, invoiceDetail.product.tax)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 10, invoiceDetail.tax_price)
            tableUtil.setTableItemValue(invoinceDetailTableWidget, i, 11, invoiceDetail.contain_tax_price)
