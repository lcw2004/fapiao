# -*- coding: UTF-8 -*-

from invoice.bean.beans import *
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
    invoice_list = list(Invoice.select().where((Invoice.status == 1) | (Invoice.status == -1), Invoice.start_time.between(start_num, end_time)))
    for invoice in invoice_list:
        print "=================================================="
        printObject(invoice)
        printObject(invoice.custom)

def testInvoiceDetail():
    idList = [1, 2, 3, 4]
    mainInvoice = Invoice.get(id=2)
    # q = InvoiceDetail.update(invoice=mainInvoice).where(InvoiceDetail.invoice in idList[1:])
    # q = InvoiceDetail.update(tax_price = 1)
    # q.execute()
    list = InvoiceDetail.select(InvoiceDetail.id).where(InvoiceDetail.id << idList[1:])
    for i in list:
        print i.id, i.pro_num

    q = InvoiceDetail.update(invoice=mainInvoice).where(InvoiceDetail.id << idList[1:])
    q.execute()
    pass


def testNoSection():
    list = NoSection.select()
    for i in list:
        print i.id, i.pro_num

if __name__ == "__main__":
    testInvoice()





