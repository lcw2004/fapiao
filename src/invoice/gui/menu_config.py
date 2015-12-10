# -*- coding: utf-8 -*-
import logging

from PyQt4.QtGui import QDialog, QFont
from invoice.common import common_util
from invoice.common import table_util
from invoice.common.settings import Settings

from menu_config_ui import *


class MenuConfigDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, custom_id=None):
        super(MenuConfigDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.init_data()

        # 绑定事件
        self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accepted)

    def accepted(self):
        """
        确定按钮事件
        :return:
        """
        try:
            invoice_start_num = table_util.get_edit_text(self.start_num_lineEdit)
            invoice_end_num = table_util.get_edit_text(self.end_num_lineEdit)
            temp_font_size = table_util.get_edit_text(self.temp_img_font_size_lineEdit)
            interface_input_path = table_util.get_edit_text(self.interface_input_lineEdit)
            interface_output_path = table_util.get_edit_text(self.interface_output_lineEdit)
            interface_temp_path = table_util.get_edit_text(self.interface_temp_lineEdit)
            temp_font_name = self.temp_img_font_ComboBox.currentFont().family()

            Settings.set_value(Settings.INVOICE_START_NUM, invoice_start_num)
            Settings.set_value(Settings.INVOICE_END_NUM, invoice_end_num)
            Settings.set_value(Settings.TEMP_FONT_SIZE, temp_font_size)
            Settings.set_value(Settings.TEMP_FONT_NAME, temp_font_name)
            Settings.set_value(Settings.INTERFACE_INPUT_PATH, interface_input_path)
            Settings.set_value(Settings.INTERFACE_OUTPUT_PATH, interface_output_path)
            Settings.set_value(Settings.INTERFACE_TEMP_PATH, interface_temp_path)
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.exception(u"报错客户信息出错！")
            logger.error(e)

    def init_data(self):
        """
        将默认的配置信息初始化到Dialog中
        :return:
        """
        try:
            invoice_start_num = common_util.to_string_trim(Settings.value_str(Settings.INVOICE_START_NUM))
            invoice_end_num = common_util.to_string_trim(Settings.value_str(Settings.INVOICE_END_NUM))
            temp_font_size = common_util.to_string_trim(Settings.value_str(Settings.TEMP_FONT_SIZE))
            temp_font_name = common_util.to_string_trim(Settings.value_str(Settings.TEMP_FONT_NAME))
            interface_input_path = common_util.to_string_trim(Settings.value_str(Settings.INTERFACE_INPUT_PATH))
            interface_output_path = common_util.to_string_trim(Settings.value_str(Settings.INTERFACE_OUTPUT_PATH))
            interface_temp_path = common_util.to_string_trim(Settings.value_str(Settings.INTERFACE_TEMP_PATH))

            self.start_num_lineEdit.setText(invoice_start_num)
            self.end_num_lineEdit.setText(invoice_end_num)
            self.temp_img_font_ComboBox.setCurrentFont(QFont(temp_font_name))
            self.temp_img_font_size_lineEdit.setText(temp_font_size)
            self.interface_input_lineEdit.setText(interface_input_path)
            self.interface_output_lineEdit.setText(interface_output_path)
            self.interface_temp_lineEdit.setText(interface_temp_path)
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.exception(u"程序出现异常")
            logger.error(e)
