# -*- coding: utf-8 -*-

from invoice.common import config
from invoice.common import common_util
from mako.template import Template


def export_as_str(invoice_list):
    """
    将发票信息导出为一个字符串
    :param invoice_list:发票信息列表
    :return:
    """
    temp = Template(filename=config.PATH_OF_XML, input_encoding='utf-8', output_encoding='utf-8')
    return temp.render(invoiceList=invoice_list)


def export_as_file(invoice_list, file_name):
    """
    将发票信息导出为一个文件
    :param invoice_list:发票信息列表
    :param file_name:文件名称
    :return:
    """
    path = config.INTERFACE_INPUT_PATH + file_name
    content = export_as_str(invoice_list)
    common_util.save_to_file(content, path)
    return common_util.is_file_exists(path)
