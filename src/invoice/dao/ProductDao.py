# -*- coding: UTF-8 -*-

import sqlite3
from BaseDao import BaseDao
from invoice.common import config
from invoice.bean.ProductBean import Product

class ProductDao(BaseDao):

    def __init__(self):
        self.connect = sqlite3.connect(config.DATABASE_PATH)

    # 保存产品
    def save(self, product):
        sql = '''
            INSERT INTO tbl_product
            (name, code, type, unit_price, tax_price, tax, business_tax_num, erp_id, col1, col2, col3, col4)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''

        cursor = self.connect.cursor()
        cursor.execute(sql, [
            product.name,
            product.code,
            product.type,
            product.unit_price,
            product.tax_price,
            product.tax,
            product.business_tax_num,
            product.erp_id,
            product.col1,
            product.col2,
            product.col3,
            product.col4
        ])
        data_id = cursor.lastrowid
        cursor.close()
        self.connect.commit()
        return data_id

    def get(self):
        sql = 'SELECT id, name, code, type, unit_price, tax_price, tax, business_tax_num, erp_id, col1, col2, col3, col4 FROM tbl_product WHERE 1=1 '

        cursor = self.connect.cursor()
        cursor.execute(sql)

        all = cursor.fetchall()
        list = []
        for row in all:
            product = Product()
            product.id = row[0]
            product.name = row[1]
            product.code = row[2]
            product.type = row[3]
            product.unit_price = row[4]
            product.tax_price = row[5]
            product.tax = row[6]
            product.business_tax_num = row[7]
            product.erp_id = row[8]
            product.col1 = row[9]
            product.col2 = row[10]
            product.col3 = row[11]
            product.col4 = row[12]
            list.append(product)
        cursor.close()
        return list
