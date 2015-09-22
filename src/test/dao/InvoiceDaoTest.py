# -*- coding: UTF-8 -*-
from invoice.dao.InvoiceDao import InvoiceDao

if __name__ == "__main__":
    invoiceDao = InvoiceDao()
    print invoiceDao.get()