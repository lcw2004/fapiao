# -*- coding: UTF-8 -*-

APPEND_EQULE = "="
APPEND_LIKE = "like"

def buildParamSQL(paramName, equleType, paramValue):
    sql = ""
    if paramValue is None:
        return sql

    if equleType == APPEND_EQULE:
        sql = " and {} {} '{}' ".format(paramName, equleType, paramValue)
    elif equleType == APPEND_LIKE:
        sql = " and {} {} '%{}%' ".format(paramName, equleType, paramValue)

    return sql