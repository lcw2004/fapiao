# -*- coding: utf-8 -*-

# 菜单栏
# C:\Python27\Lib\site-packages\PyQt4\examples\demos\textedit

# 弹出框
# C:\Python27\Lib\site-packages\PyQt4\examples\dialogs

__author__ = 'Administrator'

from PyQt4 import QtCore, QtGui
from invoice.gui.mainwindow import MainWindow



# 主程序入口
if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding('GBK')

    app = QtGui.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


