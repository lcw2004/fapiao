# -*- coding: UTF-8 -*-

import sqlite3
from BaseDao import BaseDao

zidian_db_path = "bwg.db"


class BWGProductDao(BaseDao):

    def __init__(self):
        super(self)

    # 根据产品名称查询
    def get(self, productName):
        sql = 'SELECT prudoctName, canOrder, RAM, HDD, CPU, BW, Cost_Monthly, Cost_Quarterly, Cost_Half_Year, Cost_Year, AvaliableCount FROM Product WHERE prudoctName = ?'
        cursor = self.connect.cursor()
        cursor.execute(sql, [productName])

        one = cursor.fetchone()
        product = {}
        if one:
            product["prudoctName"] = one[0]
            product["canOrder"] = one[1]
            product["RAM"] = one[2]
            product["HDD"] = one[3]
            product["CPU"] = one[4]
            product["BW"] = one[5]
            product["Cost_Monthly"] = one[6]
            product["Cost_Quarterly"] = one[7]
            product["Cost_Half_Year"] = one[8]
            product["Cost_Year"] = one[9]
            product["AvaliableCount"] = one[10]
        cursor.close()
        return product
