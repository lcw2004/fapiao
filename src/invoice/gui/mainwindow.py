# -*- coding: utf-8 -*-

from PyQt4.QtGui import QMainWindow, QMessageBox
from PyQt4 import QtCore
from PyQt4 import QtGui
from invoice.sys import ExportAsXML

from mainwindow_ui import Ui_MainWindow
from invoice.common import util
from invoice.bean.InvoiceBean import Invoice
from invoice.bean.InvoiceDetailBean import InvoiceDetail
from invoice.bean.CustomBean import Custom
from invoice.dao.InvoiceDao import InvoiceDao
from invoice.dao.InvoiceDetailDao import InvoiceDetailDao
from invoice.dao.CustomDao import CustomDao

def qStringToString(input_str):
    output_str = ""
    if input_str:
        output_str = unicode(input_str)
    return output_str



def setHeaderText(excelTableWidget, index, headerText):
    print index, headerText
    item = excelTableWidget.horizontalHeaderItem(index)
    if item:
        item.setText(translate(headerText))

def translate(text):
    _encoding = QtGui.QApplication.UnicodeUTF8
    return QtGui.QApplication.translate(None, text, None, _encoding)

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 绑定选择Excel事件
        def selectExcel():
            # TODO 判断是否选择文件
            filename = QtGui.QFileDialog.getOpenFileName(self, 'Excel', '../', 'Excel File (*.xls)')
            if filename:
                util.parseExcel(filename, self.excelTableWidget)
        self.connect(self.selectExcelFileButton, QtCore.SIGNAL("clicked()"), selectExcel)

        # 数据导入 - 生成发票
        def genInvoice():
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

            for i in range(rowCount):
                tbl_custom_name = qStringToString(excelTableWidget.item(i, 0).text())
                tbl_invoice_invoice_num = qStringToString(excelTableWidget.item(i, 1).text())
                tbl_invoice_total_not_tax = qStringToString(excelTableWidget.item(i, 2).text())
                tbl_invoice_detail_pro_type = qStringToString(excelTableWidget.item(i, 3).text())
                tbl_invoice_detail_pro_name = qStringToString(excelTableWidget.item(i, 4).text())
                tbl_invoice_remark = qStringToString(excelTableWidget.item(i, 5).text())

                # 保存用户信息
                custom = Custom()
                custom.name = tbl_custom_name
                cuntomDao.id = cuntomDao.save(custom)

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
                invoiceDetailDao.save(invoiceDetail)

                print type(tbl_custom_name)
                print tbl_invoice_invoice_num
                print tbl_invoice_total_not_tax
                print tbl_invoice_detail_pro_type
                print tbl_invoice_detail_pro_name
                print tbl_invoice_remark
                print "-------------------------------"

            QMessageBox.information(self, "Information", u'数据已经保存到临时数据区！')
        self.connect(self.genInvoiceButton, QtCore.SIGNAL("clicked()"), genInvoice)


        # 临时待处理数据 - 表格加载
        def queryInvoice():
            invoiceTableWidget = self.invoiceTableWidget

            # 查询数据
            invoiceDao = InvoiceDao()
            invoiceList = invoiceDao.get(0)

            # 将数据填充到表格中
            invoiceCount = len(invoiceList)
            self.invoiceTableWidget.setRowCount(invoiceCount)
            for i in range(invoiceCount):
                invoice = invoiceList[i]
                setTableItemValue(invoiceTableWidget, i, 0, invoice.id)
                setTableItemValue(invoiceTableWidget, i, 1, invoice.invoice_num)
                if invoice.custom:
                    setTableItemValue(invoiceTableWidget, i, 2, invoice.custom.name)
                    setTableItemValue(invoiceTableWidget, i, 7, invoice.custom.code)
                    setTableItemValue(invoiceTableWidget, i, 8, invoice.custom.tax_id)
                    setTableItemValue(invoiceTableWidget, i, 9, invoice.custom.addr)
                    setTableItemValue(invoiceTableWidget, i, 10, invoice.custom.bank_account)

                setTableItemValue(invoiceTableWidget, i, 3, invoice.total_not_tax)
                setTableItemValue(invoiceTableWidget, i, 4, invoice.total_tax)
                setTableItemValue(invoiceTableWidget, i, 5, invoice.total_num)
                setTableItemValue(invoiceTableWidget, i, 6, invoice.serial_number)

                setTableItemValue(invoiceTableWidget, i, 11, invoice.remark)
                setTableItemValue(invoiceTableWidget, i, 12, invoice.drawer)
                setTableItemValue(invoiceTableWidget, i, 13, invoice.beneficiary)
                setTableItemValue(invoiceTableWidget, i, 14, invoice.reviewer)
        self.connect(self.invoice_filter_Button, QtCore.SIGNAL("clicked()"), queryInvoice)


        # 临时待处理数据 - 修改
        def updateInvoince():
            pass
        self.connect(self.invoince_update_btn, QtCore.SIGNAL("clicked()"), queryInvoice)

        # 临时待处理数据 - 删除
        def on_action_Delete_Invoice():
            reply = QMessageBox.question(self,u'提示',u'确定要删除所选记录吗？',QMessageBox.Yes|QMessageBox.No)
            if reply == QMessageBox.Yes:
                invoiceTableWidget = self.invoiceTableWidget

                # 获取所有需要删除的行的ID
                idList = []
                remove_rows = util.getSelectedRows(invoiceTableWidget)
                for rowCount in remove_rows:
                    invoince_id = qStringToString(invoiceTableWidget.item(rowCount, 0).text())
                    if invoince_id:
                        idList.append(int(invoince_id))

                # 删除数据库中的数据
                invoiceDao = InvoiceDao()
                invoiceDao.updateStatus(idList, -1)

                # 重新加载表格
                queryInvoice()
        self.connect(self.invoince_delete_btn, QtCore.SIGNAL("clicked()"), on_action_Delete_Invoice)

        # 临时待处理数据 - 导入到开票系统
        def exportInvoinceAsXml():
            invoiceDao = InvoiceDao()
            invoinceList = invoiceDao.getAllData(0)
            isSuccess =  ExportAsXML.exportAsFile(invoinceList, "1.xml")
            if isSuccess:
                QMessageBox.information(self, "Information", u'导入成功！')
            else:
                QMessageBox.information(self, "Information", u'导入失败，请重试！')
        self.connect(self.invoince_import_xml_btn, QtCore.SIGNAL("clicked()"), exportInvoinceAsXml)

# 往表格里面填值，如果是其他类型，将其转换为str
def setTableItemValue(tableWidget, rowNum, colNum, value):
    valueStr = str(value)

    if value:
        tableWidget.setItem(rowNum, colNum, QtGui.QTableWidgetItem(valueStr))
