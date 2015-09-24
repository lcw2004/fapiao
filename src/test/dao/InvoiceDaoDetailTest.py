# -*- coding: UTF-8 -*-
from invoice.bean.InvoiceDetailBean import InvoiceDetail
from invoice.dao.InvoiceDetailDao import InvoiceDetailDao

def testSave():
    invoiceDetail = InvoiceDetail()
    invoiceDetail.pro_code = "pro_code"
    invoiceDetail.pro_name = "pro_name"
    invoiceDetail.pro_type = "pro_type"
    invoiceDetail.pro_unit = "pro_unit"
    invoiceDetail.pro_unit_price = "pro_unit_price"
    invoiceDetail.pro_num = "pro_num"
    invoiceDetail.tax_price = "tax_price"
    invoiceDetail.tax_rate = "tax_rate"
    invoiceDetail.tax = "tax"
    invoiceDetail.invoice_Id = 1

    invoiceDetailDao = InvoiceDetailDao()
    invoiceDetailDao.save(invoiceDetail)

def testGet():
    invoiceDetailDao = InvoiceDetailDao()
    invoiceDetailList = invoiceDetailDao.get()
    for invoiceDetail in invoiceDetailList:
        print "------------------------"
        print invoiceDetail.id
        print invoiceDetail.pro_code
        print invoiceDetail.pro_name
        print invoiceDetail.pro_type
        print invoiceDetail.pro_unit
        print invoiceDetail.pro_unit_price
        print invoiceDetail.pro_num
        print invoiceDetail.tax_price
        print invoiceDetail.tax_rate
        print invoiceDetail.tax
        print invoiceDetail.invoice_Id

if __name__ == "__main__":
    testSave()
    testGet()