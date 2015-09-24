# -*- coding: UTF-8 -*-

import sqlite3
from BaseDao import BaseDao
from BaseDao import appendSQL as appendSQL
from invoice.common import config
from invoice.bean.DictBean import Dict

class DictDao(BaseDao):

    def __init__(self):
        self.connect = sqlite3.connect(config.DATABASE_PATH)

    # 根据产品名称查询
    def list(self, type=None, label=None):
        sql = 'SELECT id, label, value, type, describe, status, oindex FROM tbl_dict WHERE 1=1 '
        sql += appendSQL("type", "=", type)
        sql += appendSQL("label", "=", label)

        cursor = self.connect.cursor()
        cursor.execute(sql)

        all = cursor.fetchall()
        dicts = []
        for one in all:
            dict = Dict()
            dict.id = one[0]
            dict.label = one[1]
            dict.value = one[2]
            dict.type = one[3]
            dict.describe = one[4]
            dict.status = one[5]
            dict.oindex = one[6]
            dicts.append(dict)
        cursor.close()
        return dicts

    def one(self, type=None, label=None):
        dicts = self.list(type, label)
        if dicts:
            one = dicts[0]
        return one

    def getExcelConfig(self, type=None, label=None):
        sql = 'SELECT ID, label, value, type, describe, status, oindex FROM tbl_dict WHERE 1=1 and value is not NULL '
        sql += appendSQL("type", "=", type)
        sql += appendSQL("label", "=", label)

        cursor = self.connect.cursor()
        cursor.execute(sql)

        all = cursor.fetchall()
        dicts = {}
        for one in all:
            dict = Dict()
            dict.id = one[0]
            dict.label = one[1]
            dict.value = one[2]
            dict.type = one[3]
            dict.describe = one[4]
            dict.status = one[5]
            dict.oindex = one[6]
            dicts[dict.label] = dict
        cursor.close()
        return dicts