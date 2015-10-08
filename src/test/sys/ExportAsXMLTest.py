# -*- coding: utf-8 -*-
from invoice.dao.InvoiceDao import InvoiceDao
from invoice.sys import ExportAsXML
from invoice.common import util

def testGet():
    invoiceDao = InvoiceDao()
    invoinceList = invoiceDao.getAllData(0)
    content =  ExportAsXML.getMailHtml(invoinceList)
    util.saveAsTemp(content, "D:\\1.xml")

if __name__ == "__main__":
    testGet()
