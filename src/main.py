# -*- coding: utf-8 -*-

# 菜单栏
# C:\Python27\Lib\site-packages\PyQt4\examples\demos\textedit

# 弹出框
# C:\Python27\Lib\site-packages\PyQt4\examples\dialogs

__author__ = 'Administrator'

from PyQt4 import QtCore, QtGui

from invoice.gui.mainwindow_ui import Ui_MainWindow
from src.invoice import selectFile


# 设置系统默认编码
import sys

def setSysEncoding():
    import sys
    reload(sys)
    sys.setdefaultencoding('GBK')

class Window(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)


def showMsg():
    filename = QtGui.QFileDialog.getOpenFileName(None, '选择Excel文件', '../', 'Excel File (*.xls)')



# 主程序入口
if __name__ == '__main__':
    setSysEncoding()

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()


    colums = [u'日期', u'编号', u'品名', u'类别', u'支出', u'收入', u'余额']
    # window.excelTableView = records.RecordTableModel(colums)


    # 绑定选择Excel事件
    window.connect(window.selectExcelFileButton, QtCore.SIGNAL("clicked()"), selectFile.showMsg)


