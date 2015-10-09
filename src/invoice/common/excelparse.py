# -*- coding: UTF-8 -*-

import xlrd
import commonUtil
from invoice.bean.CustomBean import Custom
from invoice.bean.InvoiceBean import Invoice
from invoice.bean.InvoiceDetailBean import InvoiceDetail
from invoice.common import tableUtil
from invoice.dao.DictDao import DictDao

from PyQt4 import QtGui

def parseExcelToInvoiceList(excelPath):
    invoiceDetailList = []

    data = xlrd.open_workbook(excelPath)

    # 获取第一个表格
    excelSheet0 = data.sheets()[0]
    nrows = excelSheet0.nrows
    ncols = excelSheet0.ncols

    for i in range(nrows):
        row = excelSheet0.row_values(i)

        tbl_custom_name = commonUtil.to_string_trim(row[4])
        tbl_invoice_invoice_num = commonUtil.float_to_string(row[3])
        tbl_invoice_total_not_tax = commonUtil.to_string_trim(row[20])
        tbl_invoice_detail_pro_type = commonUtil.to_string_trim(row[17])
        tbl_invoice_detail_pro_name = commonUtil.to_string_trim(row[16])
        tbl_invoice_remark = commonUtil.to_string_trim(row[9]) + "," + commonUtil.to_string_trim(row[6]) + "," + commonUtil.to_string_trim(row[7]) + "," + \
                             commonUtil.to_string_trim(row[12]) + "," + commonUtil.to_string_trim(row[11]) + "," + commonUtil.to_string_trim(row[14])

         # 如果是空字符串，退出
        if commonUtil.is_blank_str(tbl_invoice_invoice_num):
            continue

        # 检查是否包含中文字符串，如果包含，退出
        if commonUtil.has_chinese_charactar(tbl_invoice_invoice_num):
            continue

        # 客户对象
        custom = Custom()
        custom.name = tbl_custom_name

        # 保存发票
        invoice = Invoice()
        invoice.invoice_num = tbl_invoice_invoice_num
        invoice.remark = tbl_invoice_remark
        invoice.total_not_tax = tbl_invoice_total_not_tax
        invoice.custom = custom

        # 保存发票详细信息
        invoiceDetail = InvoiceDetail()
        invoiceDetail.pro_type = tbl_invoice_detail_pro_type
        invoiceDetail.pro_name = tbl_invoice_detail_pro_name
        invoiceDetail.invoice = invoice

        invoiceDetailList.append(invoiceDetail)

        print "--------------------------------------"
        print invoiceDetail.invoice.custom.name
        print invoiceDetail.invoice.invoice_num
        print invoiceDetail.invoice.total_not_tax
        print invoiceDetail.invoice.remark
        print invoiceDetail.pro_type
        print invoiceDetail.pro_name
        print "--------------------------------------"
    return invoiceDetailList

def parseExcel(excelPath, excelTableWidget):
    dictDao = DictDao()
    dicts = dictDao.getExcelConfig(type="EXCEL_TO_XML")

    # 设置表格头部
    tableUtil.initTableHeaders(dicts, excelTableWidget)

    # 解析Excel
    invoiceDetailList = parseExcelToInvoiceList(excelPath)

    # 设置表格行数
    nrows = len(invoiceDetailList)
    ncols = 10
    excelTableWidget.setRowCount(nrows)
    excelTableWidget.setColumnCount(ncols)
    for i in range(nrows):
        invoiceDetail = invoiceDetailList[i]

        print invoiceDetail.invoice.custom.name
        print invoiceDetail.invoice.invoice_num
        print str(invoiceDetail.invoice.total_not_tax)
        print invoiceDetail.pro_type
        print invoiceDetail.pro_name
        print invoiceDetail.invoice.remark

        excelTableWidget.setItem(i, 0, QtGui.QTableWidgetItem(invoiceDetail.invoice.custom.name))
        excelTableWidget.setItem(i, 1, QtGui.QTableWidgetItem(invoiceDetail.invoice.invoice_num))
        excelTableWidget.setItem(i, 2, QtGui.QTableWidgetItem(str(invoiceDetail.invoice.total_not_tax)))
        excelTableWidget.setItem(i, 3, QtGui.QTableWidgetItem(invoiceDetail.pro_type))
        excelTableWidget.setItem(i, 4, QtGui.QTableWidgetItem(invoiceDetail.pro_name))
        excelTableWidget.setItem(i, 5, QtGui.QTableWidgetItem(invoiceDetail.invoice.remark))