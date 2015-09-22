# -*- coding: UTF-8 -*-

import sqlite3
from BaseDao import BaseDao
from BaseDao import appendSQL as appendSQL
from invoice.common import config

class InvoiceDao(BaseDao):

    def __init__(self):
        self.connect = sqlite3.connect(config.DATABASE_PATH)


    def save(self):
        pass

    # 根据产品名称查询
    def get(self):
        sql = 'SELECT id, invoice_num, custom_id, remark, start_time, total_not_tax, total_tax, total_num, serial_number, drawer, beneficiary, reviewer, status FROM tbl_invoice WHERE 1=1 '

        cursor = self.connect.cursor()
        cursor.execute(sql)

        all = cursor.fetchall()
        dicts = []
        for one in all:
            dict = {}
            dict["id"] = one[0]
            dict["invoice_num"] = one[1]
            dict["custom_id"] = one[2]
            dict["remark"] = one[3]
            dict["start_time"] = one[4]
            dict["total_not_tax"] = one[5]
            dict["total_tax"] = one[6]
            dict["total_num"] = one[7]
            dict["serial_number"] = one[8]
            dict["drawer"] = one[9]
            dict["beneficiary"] = one[10]
            dict["reviewer"] = one[11]
            dict["reviewer"] = one[12]
            dicts.append(dict)
        cursor.close()
        return dicts
