# -*- coding: UTF-8 -*-

APPEND_EQULE = "="
APPEND_LIKE = "like"

# 构建SQL查询条件
def buildParamSQL(paramName, equleType, paramValue):
    sql = ""
    if paramValue is None:
        return sql

    if equleType == APPEND_EQULE:
        sql = " and {} {} '{}' ".format(paramName, equleType, paramValue)
    elif equleType == APPEND_LIKE:
        sql = " and {} {} '%{}%' ".format(paramName, equleType, paramValue)

    return sql

# 将ID列表转为SQL中需要的格式
def idListToString(idList):
    if not idList:
        return "()"

    idStr = ""
    for id in idList:
        idStr += str(id) + ","
    idStr = "(" + idStr[0: -1] + ")"
    return idStr