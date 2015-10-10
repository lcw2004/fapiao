# -*- coding: utf-8 -*-

# 菜单栏
# C:\Python27\Lib\site-packages\PyQt4\examples\demos\textedit

# 弹出框
# C:\Python27\Lib\site-packages\PyQt4\examples\dialogs
from invoice.common import config

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
    BASE_PATH = os.getcwd() + "/"
    config.BASE_PATH = BASE_PATH

    # 设置数据库文件路径
    config.DATABASE_PATH = BASE_PATH + "data.db"
    config.XML_PATH = BASE_PATH + "input.xml"

    print "BASE_PATH:" + config.BASE_PATH
    print "DATABASE_PATH:" + config.DATABASE_PATH
    print "INPUT_PATH:" + config.INPUT_PATH
    print "OUTPUT_PATH:" + config.OUTPUT_PATH
    print "TEMP_PATH:" + config.TEMP_PATH
    print "XML_PATH:" + config.XML_PATH


# 主程序入口
if __name__ == "__main__":
    init()

    app = QtGui.QApplication(sys.argv)
    from invoice.gui.mainwindow import MainWindow
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())