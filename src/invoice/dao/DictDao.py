# -*- coding: UTF-8 -*-

import sqlite3
from BaseDao import BaseDao
from BaseDao import appendSQL as appendSQL

zidian_db_path = "D:\\GitHub\\fapiao\\src\\invoice\\dao\\data.db"


class DictDao(BaseDao):

    def __init__(self):
        print zidian_db_path
        self.connect = sqlite3.connect(zidian_db_path)

    # 根据产品名称查询
    def get(self, type=None, label=None):
        sql = 'SELECT ID, label, value, type, describe, status, oindex FROM tbl_dict WHERE 1=1 '
        sql += appendSQL("type", "=", type)
        sql += appendSQL("label", "=", label)

        cursor = self.connect.cursor()
        cursor.execute(sql)

        all = cursor.fetchall()
        dicts = []
        for one in all:
            dict = {}
            dict["ID"] = one[0]
            dict["label"] = one[1]
            dict["value"] = one[2]
            dict["type"] = one[3]
            dict["describe"] = one[4]
            dict["status"] = one[5]
            dict["oindex"] = one[6]
            dicts.append(dict)
        cursor.close()
        return dicts

    def getExcelConfig(self, type=None, label=None):
        sql = 'SELECT ID, label, value, type, describe, status, oindex FROM tbl_dict WHERE 1=1 and value is not NULL '
        sql += appendSQL("type", "=", type)
        sql += appendSQL("label", "=", label)

        print sql

        cursor = self.connect.cursor()
        cursor.execute(sql)

        all = cursor.fetchall()
        dicts = {}
        for one in all:
            dict = {}
            dict["ID"] = one[0]
            dict["label"] = one[1]
            dict["value"] = one[2]
            dict["type"] = one[3]
            dict["describe"] = one[4]
            dict["status"] = one[5]
            dict["oindex"] = one[6]
            dicts[one[1]] = dict
        cursor.close()
        return dicts


if __name__ == "__main__":
    dictDao = DictDao()
    print dictDao.get(type="EXCEL_TO_XML")