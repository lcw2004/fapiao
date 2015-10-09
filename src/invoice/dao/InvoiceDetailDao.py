# -*- coding: UTF-8 -*-

import sqlite3
from BaseDao import BaseDao
from invoice.bean.ProductBean import Product
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

        # 获取客户信息
        for invoiceDetail in list:
            invoiceId = invoiceDetail.id
            productId = invoiceDetail.product_id
            product = self.getProductById(productId)

            invoiceDetail.product = product
        return list

    # 根据产品名称查询
    def getById(self, invoiceDetailId):
        sql = 'SELECT id, pro_num, not_tax_price, tax_price, contain_tax_price, invoice_Id, product_id FROM tbl_invoice_detail WHERE 1=1 '
        sql += SQLParams.buildParamSQL("id", SQLParams.APPEND_EQULE, invoiceDetailId)

        cursor = self.connect.cursor()
        cursor.execute(sql)

        one = cursor.fetchone()
        list = []
        invoiceDetail = None
        if one:
            invoiceDetail = InvoiceDetail()
            invoiceDetail.id = one[0]
            invoiceDetail.pro_num = one[1]
            invoiceDetail.not_tax_price = one[2]
            invoiceDetail.tax_price = one[3]
            invoiceDetail.contain_tax_price = one[4]
            invoiceDetail.invoice_Id = one[5]
            invoiceDetail.product_id = one[6]
            list.append(invoiceDetail)
        cursor.close()
        return invoiceDetail

        # 获取客户信息
        for invoiceDetail in list:
            invoiceId = invoiceDetail.id
            productId = invoiceDetail.product_id
            product = self.getProductById(productId)

            invoiceDetail.product = product
        return list

    def updateInvoiceId(self, ids, newInvoiceId):
        sql = '''UPDATE tbl_invoice_detail SET invoice_Id = ? WHERE id IN ''' + SQLParams.idListToString(ids)

        cursor = self.connect.cursor()
        cursor.execute(sql, [newInvoiceId])
        cursor.close()
        self.connect.commit()


        pass

    def getProductById(self, id):
        sql = 'SELECT id, name, code, type, unit_price, tax_price, tax, business_tax_num, erp_id, col1, col2, col3, col4 FROM tbl_product WHERE 1=1 '
        sql += " and id = ?"

        cursor = self.connect.cursor()
        cursor.execute(sql, [id])

        one = cursor.fetchone()
        product = None
        if one:
            product = Product()
            product.id = one[0]
            product.name = one[1]
            product.code = one[2]
            product.type = one[3]
            product.unit_price = one[4]
            product.tax_price = one[5]
            product.tax = one[6]
            product.business_tax_num = one[7]
            product.erp_id = one[8]
            product.col1 = one[9]
            product.col2 = one[10]
            product.col3 = one[11]
            product.col4 = one[12]

        cursor.close()
        return product

    def queryChongFu(self, invoiceId):
        sql = '''
            SELECT * FROM tbl_invoice_detail WHERE product_id in (
                SELECT product_id FROM tbl_invoice_detail WHERE invoice_Id = ? GROUP BY product_id HAVING count(product_id) > 1
            )
        '''

        cursor = self.connect.cursor()
        cursor.execute(sql, [invoiceId])

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