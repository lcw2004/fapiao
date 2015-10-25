# -*- coding: UTF-8 -*-

from invoice.bean.Beans import *
def printObject(obj):
    for property, value in vars(obj).iteritems():
        if property == "_data":
            print type(obj), property, ": ", value

def testProduct():
    product = Product.create(code = "0011")

    for product in Product.select():
        printObject(product)

def testDict():
    for dict in Dict.select().where(Dict.type=="EXCEL_TO_XML"):
        printObject(dict)

def testInvoice():
    for invoice in Invoice.select():
        print "=================================================="
        printObject(invoice)
        printObject(invoice.custom)

def testInvoiceDetail():
    idList = [1, 2]
    invoice1 = Invoice.get(id=1)
    print invoice1
    InvoiceDetail.update(invoice = invoice1).where(InvoiceDetail.invoice << idList).sql()


    pass


if __name__ == "__main__":
    testInvoiceDetail()
    # testInvoiceDetail()





