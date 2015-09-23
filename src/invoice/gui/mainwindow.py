# -*- coding: utf-8 -*-

from PyQt4.QtGui import QMainWindow
from PyQt4 import QtCore
from PyQt4 import QtGui

from mainwindow_ui import Ui_MainWindow
from invoice.common import util

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 绑定选择Excel事件
        def selectExcel():
            filename = QtGui.QFileDialog.getOpenFileName(self, 'Excel', '../', 'Excel File (*.xls)')
            if filename:
                util.parseExcel(filename, self.excelTableWidget)

        self.connect(self.selectExcelFileButton, QtCore.SIGNAL("clicked()"), selectExcel)

        def genInvoice():
            util.importDataToDB(self.excelTableWidget)


            excelTableWidget = self.excelTableWidget
            rowCount = excelTableWidget.rowCount()
            colCount = excelTableWidget.columnCount()

            for i in range(rowCount):
                tbl_custom_name = excelTableWidget.item(i, 0).text()
                tbl_invoice_invoice_num = excelTableWidget.item(i, 1).text()
                tbl_invoice_total_not_tax = excelTableWidget.item(i, 2).text()
                tbl_invoice_detail_pro_type = excelTableWidget.item(i, 3).text()
                tbl_invoice_detail_pro_name = excelTableWidget.item(i, 4).text()
                tbl_invoice_remark = excelTableWidget.item(i, 5).text()

                print tbl_custom_name
                print tbl_invoice_invoice_num
                print tbl_invoice_total_not_tax
                print tbl_invoice_detail_pro_type
                print tbl_invoice_detail_pro_name
                print tbl_invoice_remark
                print "-------------------------------"

            pass

        self.connect(self.genInvoiceButton, QtCore.SIGNAL("clicked()"), genInvoice)
