# -*- coding: utf-8 -*-


from invoice.common import config
from invoice.common import common_util
from mako.template import Template

def export_as_str(invoice_list):
    temp = Template(filename=config.XML_PATH, input_encoding='utf-8', output_encoding='utf-8')
    return temp.render(invoiceList=invoice_list)

def export_as_file(invoice_list, file_name):
    path = config.INPUT_PATH + file_name
    content = export_as_str(invoice_list)
    common_util.save_to_file(content, path)
    return common_util.is_file_exists(path)


