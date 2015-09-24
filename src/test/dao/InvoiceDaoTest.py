# -*- coding: UTF-8 -*-
from invoice.dao.InvoiceDao import InvoiceDao
from invoice.bean.InvoiceBean import Invoice

def testSave():
    invoice = Invoice()
    invoice.invoice_num = "invoice_num"
    invoice.custom_id = "custom_id"
    invoice.remark = "remark"
    invoice.start_time = "start_time"
    invoice.total_not_tax = "total_not_tax"
    invoice.total_tax = "total_tax"
    invoice.total_num = "total_num"
    invoice.serial_number = "serial_number"
    invoice.drawer = "drawer"
    invoice.beneficiary = "beneficiary"
    invoice.reviewer = "reviewer"
    invoice.status = 3

    invoiceDao = InvoiceDao()
    invoiceDao.save(invoice)

def testGet():
    invoiceDao = InvoiceDao()
    print invoiceDao.get()

if __name__ == "__main__":
    testGet()