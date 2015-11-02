# -*- coding: utf-8 -*-
from invoice.sys import invoice_exporter
from invoice.common import common_util
from invoice.bean.beans import *


def text_export_as_str():
    invoice_list = Invoice.getAllData(0)
    content = invoice_exporter.export_as_str(invoice_list)
    common_util.save_to_file(content, "D:\\1.xml")

if __name__ == "__main__":
    text_export_as_str()
