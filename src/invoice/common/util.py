# -*- coding: UTF-8 -*-

from PyQt4 import QtGui
from PyQt4.QtGui import QTableWidgetItem
import xlrd
from invoice.common import config
from invoice.dao.DictDao import DictDao
from invoice.common import excelparse

def importDataToDB(excelTableWidget):
    pass


def parseExcelBefore(excelPath):
    pass

if __name__ == "__main__":
    parseExcelBefore("C:\\Users\\Administrator\\Desktop\\data.xls")


def parseExcel(excelPath, excelTableWidget):
    dictDao = DictDao()
    dicts = dictDao.getExcelConfig(type="EXCEL_TO_XML")

    # 设置表格头部
    initTableHeaders(dicts, excelTableWidget)


    # 设置表格行数


    # 解析Excel
    invoiceDetailList = excelparse.parseExcelBefore(excelPath)
    nrows = len(invoiceDetailList)
    ncols = 10
    excelTableWidget.setRowCount(nrows)
    excelTableWidget.setColumnCount(ncols)
    for i in range(len(invoiceDetailList)):
        invoiceDetail = invoiceDetailList[i]

        excelTableWidget.setItem(i, 0, QtGui.QTableWidgetItem(invoiceDetail.invoice.custom.name))
        excelTableWidget.setItem(i, 1, QtGui.QTableWidgetItem(invoiceDetail.invoice.invoice_num))
        excelTableWidget.setItem(i, 2, QtGui.QTableWidgetItem(str(invoiceDetail.invoice.total_not_tax)))
        excelTableWidget.setItem(i, 3, QtGui.QTableWidgetItem(invoiceDetail.pro_type))
        excelTableWidget.setItem(i, 4, QtGui.QTableWidgetItem(invoiceDetail.pro_name))
        excelTableWidget.setItem(i, 5, QtGui.QTableWidgetItem(invoiceDetail.invoice.remark))

def parseExcelOld(excelPath, excelTableWidget):
    data = xlrd.open_workbook(excelPath)

    dictDao = DictDao()
    dicts = dictDao.getExcelConfig(type="EXCEL_TO_XML")
    EXCEL_START_ROW_NUM = int(config.getConfigInDB("EXCEL_START_ROW_NUM").value)

    # 设置表格行数
    excelSheet0 = data.sheets()[0]
    nrows = excelSheet0.nrows
    ncols = excelSheet0.ncols
    excelTableWidget.setRowCount(nrows - EXCEL_START_ROW_NUM)
    excelTableWidget.setColumnCount(ncols)

    # 设置表格头部
    initTableHeaders(dicts, excelTableWidget)

    for i in range(EXCEL_START_ROW_NUM, nrows):
        # 插入一行
        row = excelSheet0.row_values(i)

        tbl_custom_name = decodeCellValue(row[4])
        tbl_invoice_invoice_num = decodeCellValue(row[3])
        tbl_invoice_total_not_tax = decodeCellValue(row[20])
        tbl_invoice_detail_pro_type = decodeCellValue(row[17])
        tbl_invoice_detail_pro_name = decodeCellValue(row[16])
        tbl_invoice_remark = decodeCellValue(row[9]) + "," + decodeCellValue(row[6]) + "," + decodeCellValue(row[7]) + "," + \
                             decodeCellValue(row[12]) + "," + decodeCellValue(row[11]) + "," + decodeCellValue(row[14])

        excelTableWidget.setItem(i, 0, QtGui.QTableWidgetItem(tbl_custom_name))
        excelTableWidget.setItem(i, 1, QtGui.QTableWidgetItem(tbl_invoice_invoice_num))
        excelTableWidget.setItem(i, 2, QtGui.QTableWidgetItem(tbl_invoice_total_not_tax))
        excelTableWidget.setItem(i, 3, QtGui.QTableWidgetItem(tbl_invoice_detail_pro_type))
        excelTableWidget.setItem(i, 4, QtGui.QTableWidgetItem(tbl_invoice_detail_pro_name))
        excelTableWidget.setItem(i, 5, QtGui.QTableWidgetItem(tbl_invoice_remark))

        print "--------------------------------------"
        print "Currnt:", i
        print tbl_custom_name
        print tbl_invoice_invoice_num
        print tbl_invoice_total_not_tax
        print tbl_invoice_detail_pro_type
        print tbl_invoice_detail_pro_name
        print tbl_invoice_remark
        print "--------------------------------------"



def initTableHeaders(dicts, excelTableWidget):
      # self.table.setHorizontalHeaderLabels(['SUN','MON','TUE','WED','THU','FIR','SAT'])
    tbl_custom_name_label = dicts["tbl_custom_name"].describe
    tbl_invoice_invoice_num_label = dicts["tbl_invoice_invoice_num"].describe
    tbl_invoice_total_not_tax_label = dicts["tbl_invoice_total_not_tax"].describe
    tbl_invoice_detail_pro_type_label = dicts["tbl_invoice_detail_pro_type"].describe
    tbl_invoice_detail_pro_name_label = dicts["tbl_invoice_detail_pro_name"].describe
    tbl_invoice_remark_name_label = dicts["tbl_invoice_remark"].describe

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