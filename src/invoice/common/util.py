# -*- coding: UTF-8 -*-

from PyQt4 import QtGui
from PyQt4.QtGui import QTableWidgetItem
import xlrd
from ..dao.DictDao import DictDao


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
        # for j in range(ncols):
        #     value = row[j]
        #     excelTableWidget.setItem(i, j, QtGui.QTableWidgetItem(value))

        tbl_custom_name = decodeCellValue(row[5])
        tbl_invoice_invoice_num = decodeCellValue(row[4])
        tbl_invoice_total_not_tax = decodeCellValue(row[21])
        tbl_invoice_detail_pro_type = decodeCellValue(row[18])
        tbl_invoice_detail_pro_name = decodeCellValue(row[17])
        tbl_invoice_remark = decodeCellValue(row[10]) + "," + decodeCellValue(row[7]) + "," + decodeCellValue(row[8]) + "," + \
                             decodeCellValue(row[13]) + "," + decodeCellValue(row[13]) + "," + decodeCellValue(row[15])

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

# id = dict["ID"]
# label = dict["label"]
# value = dict["value"]
# type = dict["type"]
# desc = dict["describe"]
# status = dict["status"]
# oindex = dict["oindex"]


# tbl_custom_name
# tbl_invoice_invoice_num
# tbl_invoice_total_not_tax
# tbl_invoice_detail_pro_type
# tbl_invoice_detail_pro_name
# tbl_invoice_remark
# tbl_custom_code
# tbl_custom_tax_id
# tbl_custom_addr
# tbl_custom_bank_account
# tbl_invoice_start_time
# tbl_invoice_total_tax
# tbl_invoice_total_num
# tbl_invoice_serial_number
# tbl_invoice_drawer
# tbl_invoice_beneficiary
# tbl_invoice_reviewer
# tbl_invoice_detail_pro_code
# tbl_invoice_detail_pro_unit
# tbl_invoice_detail_pro_unit_price
# tbl_invoice_detail_pro_num
# tbl_invoice_detail_tax_price
# tbl_invoice_detail_tax_rate

# tbl_custom.name
# tbl_invoice.invoice_num
# tbl_invoice.total_not_tax
# tbl_invoice_detail.pro_type
# tbl_invoice_detail.pro_name
# tbl_invoice.remark
# tbl_custom.code
# tbl_custom.tax_id
# tbl_custom.addr
# tbl_custom.bank_account
# tbl_invoice.start_time
# tbl_invoice.total_tax
# tbl_invoice.total_num
# tbl_invoice.serial_number
# tbl_invoice.drawer
# tbl_invoice.beneficiary
# tbl_invoice.reviewer
# tbl_invoice_detail.pro_code
# tbl_invoice_detail.pro_unit
# tbl_invoice_detail.pro_unit_price
# tbl_invoice_detail.pro_num
# tbl_invoice_detail.tax_price
# tbl_invoice_detail.tax_rate