# -*- coding: UTF-8 -*-

from PyQt4 import QtGui
from PyQt4.QtGui import QTableWidgetItem
import xlrd
from invoice.dao.DictDao import DictDao


def parseExcel(excelPath, excelTableWidget):
    data = xlrd.open_workbook(excelPath)

    dictDao = DictDao()
    dicts = dictDao.getExcelConfig(type="EXCEL_TO_XML")

    # 设置表格行数
    excelSheet0 = data.sheets()[0]
    nrows = excelSheet0.nrows
    ncols = excelSheet0.ncols
    excelTableWidget.setRowCount(nrows)
    excelTableWidget.setColumnCount(ncols)

    # 设置表格头部
    initTableHeaders(dicts, excelTableWidget)

    for i in range(nrows):
        # 插入一行
        row = excelSheet0.row_values(i)

        tbl_custom_name = decodeCellValue(row[4])
        tbl_invoice_invoice_num = decodeCellValue(row[3])
        tbl_invoice_total_not_tax = decodeCellValue(row[20])
        tbl_invoice_detail_pro_type = decodeCellValue(row[17])
        tbl_invoice_detail_pro_name = decodeCellValue(row[16])
        tbl_invoice_remark = decodeCellValue(row[9]) + "," + decodeCellValue(row[6]) + "," + decodeCellValue(row[7]) + "," + \
                             decodeCellValue(row[12]) + "," + decodeCellValue(row[11]) + "," + decodeCellValue(row[14])

        print tbl_custom_name
        print tbl_invoice_invoice_num
        print tbl_invoice_total_not_tax
        print tbl_invoice_detail_pro_type
        print tbl_invoice_detail_pro_name
        print tbl_invoice_remark
        print "--------------------------------------"

        excelTableWidget.setItem(i, 0, QtGui.QTableWidgetItem(tbl_custom_name))
        excelTableWidget.setItem(i, 1, QtGui.QTableWidgetItem(tbl_invoice_invoice_num))
        excelTableWidget.setItem(i, 2, QtGui.QTableWidgetItem(tbl_invoice_total_not_tax))
        excelTableWidget.setItem(i, 3, QtGui.QTableWidgetItem(tbl_invoice_detail_pro_type))
        excelTableWidget.setItem(i, 4, QtGui.QTableWidgetItem(tbl_invoice_detail_pro_name))
        excelTableWidget.setItem(i, 5, QtGui.QTableWidgetItem(tbl_invoice_remark))


def initTableHeaders(dicts, excelTableWidget):
    tbl_custom_name_label = dicts.get("tbl_custom_name")["describe"]
    tbl_invoice_invoice_num_label = dicts.get("tbl_invoice_invoice_num")["describe"]
    tbl_invoice_total_not_tax_label = dicts.get("tbl_invoice_total_not_tax")["describe"]
    tbl_invoice_detail_pro_type_label = dicts.get("tbl_invoice_detail_pro_type")["describe"]
    tbl_invoice_detail_pro_name_label = dicts.get("tbl_invoice_detail_pro_name")["describe"]
    tbl_invoice_remark_name_label = dicts.get("tbl_invoice_remark")["describe"]

    setHeaderText(excelTableWidget, 0, tbl_custom_name_label)
    setHeaderText(excelTableWidget, 1, tbl_invoice_invoice_num_label)
    setHeaderText(excelTableWidget, 2, tbl_invoice_total_not_tax_label)
    setHeaderText(excelTableWidget, 3, tbl_invoice_detail_pro_type_label)
    setHeaderText(excelTableWidget, 4, tbl_invoice_detail_pro_name_label)
    setHeaderText(excelTableWidget, 5, tbl_invoice_remark_name_label)

def setHeaderText(excelTableWidget, index, headerText):
    print index, headerText
    item = excelTableWidget.horizontalHeaderItem(index)
    if item:
        item.setText(translate(headerText))

def translate(text):
    _encoding = QtGui.QApplication.UnicodeUTF8
    return QtGui.QApplication.translate(None, text, None, _encoding)

def decodeCellValue(uString):
    output = uString
    if type(uString) == float:
        output = str(uString)
    return output