# -*- coding: UTF-8 -*-

import sqlite3
from BaseDao import BaseDao
from BaseDao import appendSQL as appendSQL
from invoice.common import config
from invoice.bean.InvoiceDetailBean import InvoiceDetail
from invoice.bean.CustomBean import Custom

class CustomDao(BaseDao):

    def __init__(self):
        self.connect = sqlite3.connect(config.DATABASE_PATH)

    # 保存产品
    def save(self, custom):
        sql = '''
            INSERT INTO tbl_custom
            (code, name, tax_id, addr, bank_account, business_tax_di, erp_id, summary_title)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            '''

        cursor = self.connect.cursor()
        cursor.execute(sql, [
            custom.code,
            custom.name,
            custom.tax_id,
            custom.addr,
            custom.bank_account,
            custom.business_tax_di,
            custom.erp_id,
            custom.summary_title
        ])
        cursor.close()
        self.connect.commit()

    def get(self):
        sql = 'SELECT id, code, name, tax_id, addr, bank_account, business_tax_di, erp_id, summary_title FROM tbl_custom WHERE 1=1 '

        cursor = self.connect.cursor()
        cursor.execute(sql)

        all = cursor.fetchall()
        list = []
        for row in all:
            custom = Custom()
            custom.id = row[0]
            custom.code = row[1]
            custom.name = row[2]
            custom.tax_id = row[3]
            custom.addr = row[4]
            custom.bank_account = row[5]
            custom.business_tax_di = row[6]
            custom.erp_id = row[7]
            custom.summary_title = row[8]
            list.append(custom)
        cursor.close()
        return list