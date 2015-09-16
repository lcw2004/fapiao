# -*- coding: utf-8 -*-
from PyQt4 import QtGui

from src.invoice.gui import util


def showMsg():
    filename = QtGui.QFileDialog.getOpenFileName(None, '选择Excel文件', '../', 'Excel File (*.xls)')
    util.parseExcel(filename)
