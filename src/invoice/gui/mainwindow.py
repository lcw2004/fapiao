# -*- coding: utf-8 -*-

from PyQt4.QtGui import QMainWindow, QMessageBox
from PyQt4 import QtCore
from PyQt4 import QtGui

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

            QMessageBox.information(self, "Information", u'数据已经报存到临时数据区！')
        self.connect(self.genInvoiceButton, QtCore.SIGNAL("clicked()"), genInvoice)

