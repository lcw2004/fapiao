# -*- coding: utf-8 -*-


from PyQt4 import QtGui
from invoice.common.config import getConfigInDB as getConfigInDB


def init_table_headers(excel_table_widget):
    """
    设置表格头部
    :param excel_table_widget:
    :return:
    """
    # self.table.setHorizontalHeaderLabels(['SUN','MON','TUE','WED','THU','FIR','SAT'])

    tbl_custom_name_label = getConfigInDB("tbl_custom_name").describe
    tbl_invoice_invoice_num_label = getConfigInDB("tbl_invoice_invoice_num").describe
    tbl_invoice_total_not_tax_label = getConfigInDB("tbl_invoice_total_not_tax").describe
    tbl_invoice_detail_pro_type_label = getConfigInDB("tbl_invoice_detail_pro_type").describe
    tbl_invoice_detail_pro_name_label = getConfigInDB("tbl_invoice_detail_pro_name").describe
    tbl_invoice_remark_name_label = getConfigInDB("tbl_invoice_remark").describe

    set_header_text(excel_table_widget, 0, tbl_custom_name_label)
    set_header_text(excel_table_widget, 1, tbl_invoice_invoice_num_label)
    set_header_text(excel_table_widget, 2, tbl_invoice_total_not_tax_label)
    set_header_text(excel_table_widget, 3, tbl_invoice_detail_pro_type_label)
    set_header_text(excel_table_widget, 4, tbl_invoice_detail_pro_name_label)
    set_header_text(excel_table_widget, 5, tbl_invoice_remark_name_label)


def set_header_text(table_widget, index, text):
    """
    :param table_widget:需要设置头部的表格
    :param index: 序号
    :param text: 需要添加的文本
    :return:
    """
    item = table_widget.horizontalHeaderItem(index)
    if item:
        item.setText(translate(text))


def translate(text):
    """
    需要将文本转为QT需要的格式，否则会乱码
    :param text:需要转换的文本
    :return:
    """
    _encoding = QtGui.QApplication.UnicodeUTF8
    return QtGui.QApplication.translate(None, text, None, _encoding)


def str_to_unicode_str(input_str):
    """
    将字符串转为Unicode字符串
    :param input_str:需要转换的字符串
    :return:
    """
    output_str = ""
    if input_str:
        output_str = unicode(input_str)
    return output_str


def get_selected_row_number_list(table_view):
    """
    获取表格中被选中的所有行的序号
    :param table_view:
    :return:
    """
    row_number_list = []
    for index in table_view.selectedIndexes():
        if index.column() == 0:
            row_number_list.append(index.row())
    return row_number_list


def set_table_item_value(table_widget, row_num, col_num, input_str):
    """
    往表格里面填值。如果是其他类型，将其转换为str，再进行填充
    :param table_widget:表格
    :param row_num:行号
    :param col_num:列号
    :param input_str:填充的字符串
    :return:
    """
    if isinstance(input_str, unicode):
        item_text = input_str
    else:
        item_text = str(input_str)

    if input_str:
        table_widget.setItem(row_num, col_num, QtGui.QTableWidgetItem(item_text))
