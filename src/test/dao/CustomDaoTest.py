# -*- coding: UTF-8 -*-
from invoice.bean.InvoiceDetailBean import InvoiceDetail
from invoice.dao.InvoiceDetailDao import InvoiceDetailDao
from invoice.bean.CustomBean import Custom
from invoice.dao.CustomDao import CustomDao


def testSave():
    custom = Custom()
    custom.code = "code"
    custom.name = "name"
    custom.tax_id = "tax_id"
    custom.addr = "addr"
    custom.bank_account = "bank_account"
    custom.business_tax_di = "business_tax_di"
    custom.erp_id = "erp_id"
    custom.summary_title = "summary_title"

    customDao = CustomDao()
    customDao.save(custom)

def testSaveNull():
    custom = Custom()
    customDao = CustomDao()
    customDao.save(custom)
    list = customDao.get()
    for custom in list:
        print "------------------------"
        print custom.id
        print custom.code
        print custom.name
        print custom.tax_id
        print custom.addr
        print custom.bank_account
        print custom.business_tax_di
        print custom.erp_id
        print custom.summary_title

def testGet():
    customDao = CustomDao()
    list = customDao.get("")
    for custom in list:
        print "------------------------"
        print custom.id
        print custom.code
        print custom.name
        print custom.tax_id
        print custom.addr
        print custom.bank_account
        print custom.business_tax_di
        print custom.erp_id
        print custom.summary_title

def testGetOne():
     customDao = CustomDao()
     custom = customDao.getOne(name="上海瑞弘物流有限公司")
     print custom.id

if __name__ == "__main__":
    # testSaveNull()
    testGetOne()
