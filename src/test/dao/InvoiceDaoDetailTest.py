# -*- coding: UTF-8 -*-
from invoice.bean.InvoiceDetailBean import InvoiceDetail
from invoice.dao.InvoiceDetailDao import InvoiceDetailDao

def testSave():
    invoiceDetail = InvoiceDetail()
    invoiceDetail.id = None
    invoiceDetail.pro_num = 1
    invoiceDetail.not_tax_price = 2
    invoiceDetail.tax_price = 3
    invoiceDetail.contain_tax_price = 4

    invoiceDetail.product_id = 100
    invoiceDetail.invoice_Id = 1

    invoiceDetailDao = InvoiceDetailDao()
    invoiceDetailDao.save(invoiceDetail)

def testGet():
    invoiceDetailDao = InvoiceDetailDao()
    invoiceDetailList = invoiceDetailDao.get(1)
    for invoiceDetail in invoiceDetailList:
        print "------------------------"
        print invoiceDetail.id
        print invoiceDetail.pro_num
        print invoiceDetail.not_tax_price
        print invoiceDetail.tax_price
        print invoiceDetail.contain_tax_price
        print invoiceDetail.invoice_Id
        print invoiceDetail.product_id

if __name__ == "__main__":
    testSave()
    testGet()