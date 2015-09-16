# -*- coding: utf-8 -*-

from PyQt4.QtGui import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt4 import QtCore
from mainwindow_ui import Ui_MainWindow
from PyQt4 import QtGui
import util


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 绑定选择Excel事件
        def showMsg():
            filename = QtGui.QFileDialog.getOpenFileName(self, 'Excel', '../', 'Excel File (*.xls)')
            if filename:
                util.parseExcel(filename, self.excelTableWidget)
        self.connect(self.selectExcelFileButton, QtCore.SIGNAL("clicked()"), showMsg)




if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding('GBK')

    app = QtGui.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
