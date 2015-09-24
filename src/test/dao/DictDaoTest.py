# -*- coding: UTF-8 -*-
from invoice.dao.DictDao import DictDao
from invoice.bean.DictBean import Dict

def testGet():
    dictDao = DictDao()
    list = dictDao.get(type="EXCEL_TO_XML")
    for dict in list:
        print "------------------------"
        print dict.id
        print dict.label
        print dict.value
        print dict.type
        print dict.describe
        print dict.status
        print dict.oindex

def testGetExcelConfig():
    dictDao = DictDao()
    list = dictDao.getExcelConfig(type="EXCEL_TO_XML")
    for label in list:
        print "------------------------"
        dict = list[label]
        print dict.id
        print dict.label
        print dict.value
        print dict.type
        print dict.describe
        print dict.status
        print dict.oindex

if __name__ == "__main__":
    testGet()
    testGetExcelConfig()