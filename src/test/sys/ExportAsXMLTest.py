# -*- coding: utf-8 -*-
from invoice.dao.InvoiceDao import InvoiceDao
from invoice.sys import ExportAsXML

def testGet():
    invoiceDao = InvoiceDao()
    invoinceList = invoiceDao.getAllData(0)


    for invoice in invoinceList:
        print "invoice:", invoice.id


    # print ExportAsXML.getMailHtml(invoinceList)

if __name__ == "__main__":
    testGet()
