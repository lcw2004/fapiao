# -*- coding: utf-8 -*-

# 菜单栏
# C:\Python27\Lib\site-packages\PyQt4\examples\demos\textedit

# 弹出框
# C:\Python27\Lib\site-packages\PyQt4\examples\dialogs

__author__ = 'Administrator'

from PyQt4 import QtCore, QtGui

import os
import sys

# 项目基础路径
BASE_PATH = None
DATABASE_PATH = None

def init():
    # 设置项目编码
    import sys
    reload(sys)
    sys.setdefaultencoding('GBK')

    # 设置项目基础路径
    BASE_PATH = os.path.abspath(sys.argv[0])
    BASE_PATH = os.path.dirname(BASE_PATH) + "/"
    print "BASE_PATH:" + BASE_PATH

    # 设置数据库文件路径
    DATABASE_PATH = BASE_PATH + "data.db"
    print "DATABASE_PATH:" + DATABASE_PATH


# 主程序入口
if __name__ == "__main__":
    init()

    app = QtGui.QApplication(sys.argv)
    from invoice.gui.mainwindow import MainWindow
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


