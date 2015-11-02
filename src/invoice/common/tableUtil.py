# -*- coding: utf-8 -*-


from PyQt4 import QtGui
from invoice.common.config import getConfigInDB as getConfigInDB

# 设置表头
def initTableHeaders(excelTableWidget):
      # self.table.setHorizontalHeaderLabels(['SUN','MON','TUE','WED','THU','FIR','SAT'])


    tbl_custom_name_label = getConfigInDB("tbl_custom_name").describe
    tbl_invoice_invoice_num_label =  getConfigInDB("tbl_invoice_invoice_num").describe
    tbl_invoice_total_not_tax_label =  getConfigInDB("tbl_invoice_total_not_tax").describe
    tbl_invoice_detail_pro_type_label =  getConfigInDB("tbl_invoice_detail_pro_type").describe
    tbl_invoice_detail_pro_name_label =  getConfigInDB("tbl_invoice_detail_pro_name").describe
    tbl_invoice_remark_name_label =  getConfigInDB("tbl_invoice_remark").describe

    setHeaderText(excelTableWidget, 0, tbl_custom_name_label)
    setHeaderText(excelTableWidget, 1, tbl_invoice_invoice_num_label)
    setHeaderText(excelTableWidget, 2, tbl_invoice_total_not_tax_label)
    setHeaderText(excelTableWidget, 3, tbl_invoice_detail_pro_type_label)
    setHeaderText(excelTableWidget, 4, tbl_invoice_detail_pro_name_label)
    setHeaderText(excelTableWidget, 5, tbl_invoice_remark_name_label)

# 设置表头
def setHeaderText(excelTableWidget, index, headerText):
    print index, headerText
    item = excelTableWidget.horizontalHeaderItem(index)
    if item:
        item.setText(translate(headerText))

def translate(text):
    _encoding = QtGui.QApplication.UnicodeUTF8
    return QtGui.QApplication.translate(None, text, None, _encoding)

def qStringToString(input_str):
    output_str = ""
    if input_str:
        output_str = unicode(input_str)
    return output_str


# 获取表格中选取的行的序号
def getSelectedRows(tableView):
    rows = []
    for index in tableView.selectedIndexes():
        if index.column() == 0:
            rows.append(index.row())
    return rows


# 往表格里面填值，如果是其他类型，将其转换为str
def setTableItemValue(tableWidget, rowNum, colNum, value):
    valueStr = ""
    if isinstance(value, unicode):
        valueStr = value
    else:
        valueStr = str(value)

    if value:
        tableWidget.setItem(rowNum, colNum, QtGui.QTableWidgetItem(valueStr))
