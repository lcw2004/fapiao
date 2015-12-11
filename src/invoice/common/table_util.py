# -*- coding: utf-8 -*-
import datetime
from PyQt4 import QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QTableWidgetItem

from invoice.common import config
from invoice.common import common_util
from invoice.common.settings import Settings


def init_table_headers(excel_table_widget):
    """
    设置表格头部
    :param excel_table_widget:
    :return:
    """
    # self.table.setHorizontalHeaderLabels(['SUN','MON','TUE','WED','THU','FIR','SAT'])

    tbl_custom_name_label = config.get_config_from_database("tbl_custom_name").describe
    tbl_invoice_invoice_num_label = config.get_config_from_database("tbl_invoice_invoice_num").describe
    tbl_invoice_total_not_tax_label = config.get_config_from_database("tbl_invoice_total_not_tax").describe
    tbl_invoice_detail_pro_type_label = config.get_config_from_database("tbl_invoice_detail_pro_type").describe
    tbl_invoice_detail_pro_name_label = config.get_config_from_database("tbl_invoice_detail_pro_name").describe
    tbl_invoice_remark_name_label = config.get_config_from_database("tbl_invoice_remark").describe

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
    elif isinstance(input_str, datetime.datetime):
        item_text = common_util.time_to_str(input_str)
    else:
        item_text = str(input_str)

    # import logging
    # logger = logging.getLogger(__name__)
    # logger.info(str(input_str) + "[" + str(type(input_str)) + "] --> " + item_text)

    if input_str:
        item = QTableWidgetItem(item_text)
        table_widget.setItem(row_num, col_num, item)

def set_table_item_value_editable(table_widget, row_num, col_num, input_str, editable):
    """
    往表格里面填值。如果是其他类型，将其转换为str，再进行填充
    :param table_widget:表格
    :param row_num:行号
    :param col_num:列号
    :param input_str:填充的字符串
    :param editable:表格是否能编辑
    :return:
    """

    if isinstance(input_str, unicode):
        item_text = input_str
    elif isinstance(input_str, datetime.datetime):
        item_text = common_util.time_to_str(input_str)
    else:
        item_text = str(input_str)

    import logging
    logger = logging.getLogger(__name__)
    logger.info(str(input_str) + "[" + str(type(input_str)) + "] --> " + item_text)

    if input_str:
        item = QTableWidgetItem(item_text)
        table_widget.setItem(row_num, col_num, item)

        # 设置不可编辑
        if editable:
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            set_table_item_color(table_widget, row_num, col_num, QtGui.QColor(224, 224, 224))


def set_table_item_un_editable(table_widget, row_num, col_num):
    # 设置不可编辑
    item = table_widget.item(row_num, col_num)
    if item:
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        set_table_item_color(table_widget, row_num, col_num, QtGui.QColor(224, 224, 224))


def set_table_item_color(table_widget, row_num, col_num, color):
    """
    设置表格单元的背景色
    :param table_widget:表格
    :param row_num:行号
    :param col_num:列号
    :param color:填充的颜色
    :return:
    """
    table_widget.item(row_num, col_num).setBackground(color)


def get_edit_text(edit):
    """
    获取指定编辑框中的文本，并转为GBK编码
    :param edit: 编辑框
    """
    text = edit.text()
    return str(text).decode("GBK")

def get_edit_text_float(edit):
    """
    获取指定编辑框中的文本，并转为GBK编码，再转为数字类型
    :param edit: 编辑框
    """
    return float(get_edit_text(edit))

def get_paint_context(edit):
    """
    获取多行编辑框中的文本，并转为GBK编码
    :param edit: 多行编辑框
    """
    text = edit.toPlainText()
    return str(text).decode("GBK")


def load_data_setting(line_edit, set_key):
    """
    将文本框中的值存到指定的键中
    :param line_edit:文本框
    :param set_key:键
    :return:
    """
    value = common_util.to_string_trim(Settings.value_str(set_key))
    line_edit.setText(value)


def save_data_setting(line_edit, set_key):
    """
    将指定的键中的值存到文本框中
    :param line_edit:文本框
    :param set_key:键
    :return:
    """
    value = get_edit_text(line_edit)
    Settings.set_value(set_key, value)


def get_item_value(table, row_num, col_num):
    item = table.item(row_num, col_num)
    if item:
        return str(item.text()).decode("GBK")
    else:
        return ""

def get_item_value_float(table, row_num, col_num):
    value = get_item_value(table, row_num, col_num)
    if value is None or len(value) == 0:
        return 0
    else:
        return float(value)

def get_item_value_int(table, row_num, col_num):
    value = get_item_value(table, row_num, col_num)
    if value is None or len(value) == 0:
        return 0
    else:
        return int(value)