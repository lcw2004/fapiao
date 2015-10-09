# -*- coding: UTF-8 -*-

import sqlite3
from BaseDao import BaseDao
from invoice.common import config
from invoice.bean.InvoiceDetailBean import InvoiceDetail
from invoice.dao import SQLParams


class InvoiceDetailDao(BaseDao):

    def __init__(self):
        self.connect = sqlite3.connect(config.DATABASE_PATH)

    # 保存产品
    def save(self, invoiceDetail):
        sql = '''
            INSERT INTO tbl_invoice_detail
            (pro_num, not_tax_price, tax_price, contain_tax_price, invoice_Id, product_id)
            VALUES (?, ?, ?, ?, ?, ?)
            '''

        cursor = self.connect.cursor()
        cursor.execute(sql, [
            invoiceDetail.pro_num,
            invoiceDetail.not_tax_price,
            invoiceDetail.tax_price,
            invoiceDetail.contain_tax_price,
            invoiceDetail.invoice_Id,
            invoiceDetail.product_id
        ])
        data_id = cursor.lastrowid
        cursor.close()
        self.connect.commit()
        return data_id


    # 根据产品名称查询
    def get(self, invoiceId=None, productId=None):
        sql = 'SELECT id, pro_num, not_tax_price, tax_price, contain_tax_price, invoice_Id, product_id FROM tbl_invoice_detail WHERE 1=1 '
        sql += SQLParams.buildParamSQL("invoice_Id", SQLParams.APPEND_EQULE, invoiceId)
        sql += SQLParams.buildParamSQL("product_id", SQLParams.APPEND_EQULE, productId)

        cursor = self.connect.cursor()
        cursor.execute(sql)

        all = cursor.fetchall()
        list = []
        for row in all:
            invoiceDetail = InvoiceDetail()
            invoiceDetail.id = row[0]
            invoiceDetail.pro_num = row[1]
            invoiceDetail.not_tax_price = row[2]
            invoiceDetail.tax_price = row[3]
            invoiceDetail.contain_tax_price = row[4]
            invoiceDetail.invoice_Id = row[5]
            invoiceDetail.product_id = row[6]
            list.append(invoiceDetail)
        cursor.close()
        return list