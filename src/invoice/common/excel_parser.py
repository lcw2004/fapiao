# -*- coding: UTF-8 -*-

import xlrd
import common_util
from invoice.bean.beans import *


def parse_excel_to_invoice_list(excel_path):
    """
    解析Excel文件，并将Excel内的数据转为一个Invoice List
    :param excel_path:Excel文件路径
    :return:Invoice List
    """
    invoice_detail_list = []

    # 读取Excel文件
    data = xlrd.open_workbook(excel_path)

    # 获取第一个表格
    excel_sheet_0 = data.sheets()[0]
    sheet_nrows = excel_sheet_0.nrows

    for i in range(sheet_nrows):
        row = excel_sheet_0.row_values(i)

        tbl_custom_name = common_util.to_string_trim(row[4])
        tbl_invoice_invoice_num = common_util.float_to_string(row[3])
        tbl_invoice_total_not_tax = common_util.to_string_trim(row[20])
        tbl_invoice_detail_pro_type = common_util.to_string_trim(row[17])
        tbl_invoice_detail_pro_name = common_util.to_string_trim(row[16])
        tbl_invoice_remark = common_util.to_string_trim(row[9]) + "," + \
                             common_util.to_string_trim(row[6]) + "," + \
                             common_util.to_string_trim(row[7]) + "," + \
                             common_util.to_string_trim(row[12]) + "," + \
                             common_util.to_string_trim(row[11]) + "," + \
                             common_util.to_string_trim(row[14])

        # 如果是空字符串，退出
        if common_util.is_blank_str(tbl_invoice_invoice_num):
            continue

        # 检查是否包含中文字符串，如果包含，退出
        if common_util.has_chinese_charactar(tbl_invoice_invoice_num):
            continue

        # 客户对象
        custom = Custom()
        custom.name = tbl_custom_name

        # 发票对象
        invoice = Invoice()
        invoice.invoice_num = tbl_invoice_invoice_num
        invoice.remark = tbl_invoice_remark
        invoice.total_not_tax = tbl_invoice_total_not_tax
        invoice.custom = custom

        # 产品对象
        product = Product()
        product.type = tbl_invoice_detail_pro_type
        product.name = tbl_invoice_detail_pro_name

        # 保存发票详细信息
        invoice_detail = InvoiceDetail()
        invoice_detail.product = product
        invoice_detail.invoice = invoice

        invoice_detail_list.append(invoice_detail)

    return invoice_detail_list
