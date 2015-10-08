# -*- coding: UTF-8 -*-

import sqlite3
from BaseDao import BaseDao
from invoice.bean.CustomBean import Custom
from invoice.bean.InvoiceDetailBean import InvoiceDetail
from invoice.dao import SQLParams
from invoice.common import config
from invoice.bean.InvoiceBean import Invoice
from invoice.common import util

class InvoiceDao(BaseDao):

    def __init__(self):
        self.connect = sqlite3.connect(config.DATABASE_PATH)

    # 保存产品
    def save(self, invoice):
        sql = '''
            INSERT INTO tbl_invoice
            (invoice_num, custom_id, remark, start_time, total_not_tax, total_tax, total_num, serial_number, drawer, beneficiary, reviewer, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''

        cursor = self.connect.cursor()
        cursor.execute(sql, [invoice.invoice_num,
                             invoice.custom_id,
                             invoice.remark,
                             invoice.start_time,
                             invoice.total_not_tax,
                             invoice.total_tax,
                             invoice.total_num,
                             invoice.serial_number,
                             invoice.drawer,
                             invoice.beneficiary,
                             invoice.reviewer,
                             invoice.status])
        data_id = cursor.lastrowid
        cursor.close()
        self.connect.commit()
        return data_id

    # 根据产品名称查询
    def get(self, status):
        sql = 'SELECT id, invoice_num, custom_id, remark, start_time, total_not_tax, total_tax, total_num, serial_number, drawer, beneficiary, reviewer, status FROM tbl_invoice WHERE 1=1 '
        sql += SQLParams.buildParamSQL("status", SQLParams.APPEND_EQULE, status)

        cursor = self.connect.cursor()
        cursor.execute(sql)

        all = cursor.fetchall()
        list = []
        for one in all:
            invoice = Invoice()
            invoice.id = one[0]
            invoice.invoice_num = one[1]
            invoice.custom_id = one[2]
            invoice.remark = one[3]
            invoice.start_time = one[4]
            invoice.total_not_tax = one[5]
            invoice.total_tax = one[6]
            invoice.total_num = one[7]
            invoice.serial_number = one[8]
            invoice.drawer = one[9]
            invoice.beneficiary = one[10]
            invoice.reviewer = one[11]
            invoice.reviewer = one[12]
            list.append(invoice)
        cursor.close()
        return list


# 根据产品名称查询
    def getAllData(self, status):
        sql = 'SELECT id, invoice_num, custom_id, remark, start_time, total_not_tax, total_tax, total_num, serial_number, drawer, beneficiary, reviewer, status FROM tbl_invoice WHERE 1=1 '
        sql += SQLParams.buildParamSQL("status", SQLParams.APPEND_EQULE, status)

        cursor = self.connect.cursor()
        cursor.execute(sql)

        all = cursor.fetchall()
        invoiceList = []
        for one in all:
            invoice = Invoice()
            invoice.id = one[0]
            invoice.invoice_num = one[1]
            invoice.custom_id = one[2]
            invoice.remark = one[3]
            invoice.start_time = one[4]
            invoice.total_not_tax = one[5]
            invoice.total_tax = one[6]
            invoice.total_num = one[7]
            invoice.serial_number = one[8]
            invoice.drawer = one[9]
            invoice.beneficiary = one[10]
            invoice.reviewer = one[11]
            invoice.reviewer = one[12]
            invoiceList.append(invoice)
        cursor.close()

        # 获取客户信息
        for invoice in invoiceList:
            invoiceId = invoice.id
            customId = invoice.custom_id
            custom = getCustomById(self.connect, customId)
            invoiceDetailList = getInvoinceDetailListById(self.connect, invoiceId)

            invoice.invoiceDetailList = invoiceDetailList
            invoice.custom = custom
        return invoiceList




    def updateStatus(self, ids, newStatus):
        sql = '''UPDATE tbl_invoice SET status = ? WHERE id IN ''' + util.idListToString(ids)

        cursor = self.connect.cursor()
        cursor.execute(sql, [newStatus])
        cursor.close()
        self.connect.commit()



def getInvoinceDetailListById(connect, invoiceId):
    sql = 'SELECT id, pro_code, pro_name, pro_type, pro_unit, pro_unit_price, pro_num, tax_price, tax_rate, tax, invoice_Id FROM tbl_invoice_detail WHERE invoice_Id = ?'

    cursor = connect.cursor()
    cursor.execute(sql, [invoiceId])

    one = cursor.fetchall()
    invoiceDetailList = []
    for row in one:
        invoiceDetail = InvoiceDetail()
        invoiceDetail.id = row[0]
        invoiceDetail.pro_code = row[1]
        invoiceDetail.pro_name = row[2]
        invoiceDetail.pro_type = row[3]
        invoiceDetail.pro_unit = row[4]
        invoiceDetail.pro_unit_price = row[5]
        invoiceDetail.pro_num = row[6]
        invoiceDetail.tax_price = row[7]
        invoiceDetail.tax_rate = row[8]
        invoiceDetail.tax = row[9]
        invoiceDetail.invoice_Id = row[10]
        invoiceDetailList.append(invoiceDetail)

    cursor.close()

    return invoiceDetailList


def getCustomById(connect, customId):
    sql = 'SELECT id, code, name, tax_id, addr, bank_account, business_tax_di, erp_id, summary_title FROM tbl_custom WHERE id = ? '

    cursor = connect.cursor()
    cursor.execute(sql, [customId])
    one = cursor.fetchone()

    custom = None
    if one:
        custom = Custom()
        custom.id = one[0]
        custom.code = one[1]
        custom.name = one[2]
        custom.tax_id = one[3]
        custom.addr = one[4]
        custom.bank_account = one[5]
        custom.business_tax_di = one[6]
        custom.erp_id = one[7]
        custom.summary_title = one[8]

    cursor.close()

    return custom