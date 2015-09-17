# -*- coding: UTF-8 -*-

import sqlite3

zidian_db_path = "data.db"

def appendSQL(paramName, equleType, paramValue):
    sql = ""
    if paramValue:
        if equleType == "=":
            sql = " and {} {} '{}' ".format(paramName, equleType, paramValue)
        elif equleType == "like":
            sql = " and {} {} '%{}%' ".format(paramName, equleType, paramValue)
    return sql


class BaseDao:
    def __init__(self):
        self.connect = sqlite3.connect(zidian_db_path)