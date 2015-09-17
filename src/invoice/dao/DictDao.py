# -*- coding: UTF-8 -*-

import sqlite3
from BaseDao import BaseDao
from BaseDao import appendSQL as appendSQL

zidian_db_path = "data.db"


class DictDao(BaseDao):

    def __init__(self):
        self.connect = sqlite3.connect(zidian_db_path)

    # 根据产品名称查询
    def get(self, type=None, label=None):
        sql = 'SELECT ID, label, value, type, describe, status, oindex FROM tbl_dict WHERE 1=1 '
        sql += appendSQL("type", "=", type)
        sql += appendSQL("label", "like", label)

        cursor = self.connect.cursor()
        cursor.execute(sql)

        all = cursor.fetchall()
        products = []
        for one in all:
            product = {}
            product["ID"] = one[0]
            product["label"] = one[1]
            product["value"] = one[2]
            product["type"] = one[3]
            product["describe"] = one[4]
            product["status"] = one[5]
            product["oindex"] = one[6]
            products.append(product)
        cursor.close()
        return products


# if __name__ == "__main__":
#     dictDao = DictDao()
#     print dictDao.get(type="EXCEL_TO_XML", label="tbl_custom")