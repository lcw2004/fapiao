# -*- coding: UTF-8 -*-

from PyQt4 import QtGui
import xlrd
from ..dao.DictDao import DictDao

def parseExcel(excelPath, excelTableWidget):
    data = xlrd.open_workbook(excelPath)

    # 获取第一个Sheet
    excelSheet0 = data.sheets()[0]
    nrows = excelSheet0.nrows
    ncols = excelSheet0.ncols
    excelTableWidget.setRowCount(nrows)
    excelTableWidget.setColumnCount(ncols)

    for i in range(nrows):
        # 插入一行
        row = excelSheet0.row_values(i)
        for j in range(ncols):
            value = row[j]
            excelTableWidget.setItem(i, j, QtGui.QTableWidgetItem(value))
