# -*- coding: UTF-8 -*-

import sqlite3
from BaseDao import BaseDao
from BaseDao import appendSQL as appendSQL
from invoice.common import config
from invoice.bean.InvoiceBean import Invoice

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
        cursor.close()
        self.connect.commit()

    # 根据产品名称查询
    def get(self):
        sql = 'SELECT id, invoice_num, custom_id, remark, start_time, total_not_tax, total_tax, total_num, serial_number, drawer, beneficiary, reviewer, status FROM tbl_invoice WHERE 1=1 '

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
        return invoiceList
