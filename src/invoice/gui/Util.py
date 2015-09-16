# -*- coding: UTF-8 -*-

from PyQt4 import QtGui
import xlrd


def parseExcel(excelPath, excelTableWidget):
    data = xlrd.open_workbook(excelPath)

    # 获取第一个Sheet
    excelSheet0 = data.sheets()[0]
    nrows = excelSheet0.nrows
    ncols = excelSheet0.ncols
    for i in range(nrows):

        # 插入一行
        rowPosition = excelTableWidget.rowCount()
        excelTableWidget.insertRow(rowPosition)

        row = excelSheet0.row_values(i)
        for j in range(ncols):
            value = row[j]
            print value

            excelTableWidget.setItem(rowPosition, j, QtGui.QTableWidgetItem(value))