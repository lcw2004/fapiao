# -*- coding: UTF-8 -*-

from invoice.bean.beans import *
from invoice.common.settings import Settings


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
    invoice_start_num = Settings.value_str(Settings.INVOICE_START_NUM)
    invoice_end_num = Settings.value_str(Settings.INVOICE_END_NUM)
    invoice_list = Invoice.select(Invoice.invoice_num).where(Invoice.invoice_num.between(invoice_start_num, invoice_end_num)).order_by(Invoice.invoice_num.asc())
    printObject( list(invoice_list)[-1])
    for invoice in invoice_list:
        print "=================================================="
        printObject(invoice)


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

    use_num = 0

    for no_section in list:
        use_num += no_section.end_num - no_section.start_num + 1
        print no_section.start_num, no_section.end_num

    print use_num

if __name__ == "__main__":
    testInvoice()





