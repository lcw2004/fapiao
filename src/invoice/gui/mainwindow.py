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
            pass

        self.connect(self.genInvoiceButton, QtCore.SIGNAL("clicked()"), genInvoice)
