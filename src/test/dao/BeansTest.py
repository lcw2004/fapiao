# -*- coding: UTF-8 -*-

from invoice.bean.Beans import *
def printObject(obj):
    for property, value in vars(obj).iteritems():
        if property == "_data":
            print type(obj) , property, ": ", value

def testProduct():
    for product in Product.select():
        print printObject(product)

def testDict():
    for dict in Dict.select():
        print printObject(dict)

def testInvoice():
    for invoice in Invoice.select():
        print "=================================================="
        print printObject(invoice)
        print printObject(invoice.custom)

def testInvoiceDetail():
    for invoiceDetail in InvoiceDetail.select():
        print "=================================================="
        print printObject(invoiceDetail)
        print printObject(invoiceDetail.invoice)
        print printObject(invoiceDetail.product)

if __name__ == "__main__":
    # testProduct()
    testInvoiceDetail()





