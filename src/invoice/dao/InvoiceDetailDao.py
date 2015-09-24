# -*- coding: UTF-8 -*-

import sqlite3
from BaseDao import BaseDao
from BaseDao import appendSQL as appendSQL
from invoice.common import config
from invoice.bean.InvoiceDetailBean import InvoiceDetail

class InvoiceDetailDao(BaseDao):

    def __init__(self):
        self.connect = sqlite3.connect(config.DATABASE_PATH)

    # 保存产品
    def save(self, invoiceDetail):
        sql = '''
            INSERT INTO tbl_invoice_detail
            (id, pro_code, pro_name, pro_type, pro_unit, pro_unit_price, pro_num, tax_price, tax_rate, tax, invoice_Id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''

        cursor = self.connect.cursor()
        cursor.execute(sql, [
            invoiceDetail.id,
            invoiceDetail.pro_code,
            invoiceDetail.pro_name,
            invoiceDetail.pro_type,
            invoiceDetail.pro_unit,
            invoiceDetail.pro_unit_price,
            invoiceDetail.pro_num,
            invoiceDetail.tax_price,
            invoiceDetail.tax_rate,
            invoiceDetail.tax,
            invoiceDetail.invoice_Id
        ])
        data_id = cursor.lastrowid
        cursor.close()
        self.connect.commit()
        return data_id


    # 根据产品名称查询
    def get(self):
        sql = 'SELECT id, pro_code, pro_name, pro_type, pro_unit, pro_unit_price, pro_num, tax_price, tax_rate, tax, invoice_Id FROM tbl_invoice_detail WHERE 1=1 '

        cursor = self.connect.cursor()
        cursor.execute(sql)

        all = cursor.fetchall()
        list = []
        for row in all:
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
            list.append(invoiceDetail)
        cursor.close()
        return list