# -*- coding: UTF-8 -*-

import sqlite3
from BaseDao import BaseDao
from BaseDao import appendSQL as appendSQL
import main




class DictDao(BaseDao):

    def __init__(self):
        # 设置项目编码
        import sys
        reload(sys)
        sys.setdefaultencoding('GBK')

        # 设置项目基础路径
        import os
        BASE_PATH = os.path.abspath(sys.argv[0])
        BASE_PATH = os.path.dirname(BASE_PATH) + "\\"
        print "BASE_PATH:" + BASE_PATH

        # 设置数据库文件路径
        DATABASE_PATH = BASE_PATH + "data.db"
        print "DATABASE_PATH:" + DATABASE_PATH

        self.connect = sqlite3.connect(DATABASE_PATH)

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