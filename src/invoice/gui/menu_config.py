# -*- coding: utf-8 -*-
import logging

from PyQt4.QtGui import QDialog

from invoice.bean.beans import User
from invoice.common import table_util
from invoice.common.settings import Settings
from menu_config_ui import *


class MenuConfigDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, custom_id=None):
        super(MenuConfigDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.init_data()

        user_id = Settings.value_int(Settings.USER_ID)
        user = User.get(id=user_id)
        # 根据用户权限，控制是否显示“库存管理”
        if not user.is_admin:
            self.invoice_code_lineEdit.setDisabled(True)
            self.start_num_lineEdit.setDisabled(True)
            self.end_num_lineEdit.setDisabled(True)

        # 绑定事件
        self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accepted)

    def accepted(self):
        """
        确定按钮事件
        :return:
        """
        try:
            table_util.save_data_setting(self.start_num_lineEdit, Settings.INVOICE_START_NUM)
            table_util.save_data_setting(self.end_num_lineEdit, Settings.INVOICE_END_NUM)
            table_util.save_data_setting(self.temp_img_font_size_lineEdit, Settings.TEMP_FONT_SIZE)
            table_util.save_data_setting(self.temp_img_font_lineEdit, Settings.TEMP_FONT_NAME)
            table_util.save_data_setting(self.interface_input_lineEdit, Settings.INTERFACE_INPUT_PATH)
            table_util.save_data_setting(self.interface_output_lineEdit, Settings.INTERFACE_OUTPUT_PATH)
            table_util.save_data_setting(self.interface_temp_lineEdit, Settings.INTERFACE_TEMP_PATH)
            table_util.save_data_setting(self.beneficiary_lineEdit, Settings.BENEFICIARY_NAME)
            table_util.save_data_setting(self.reviewer_lineEdit, Settings.REVIEWER_NAME)
            table_util.save_data_setting(self.invoice_code_lineEdit, Settings.INVOICE_CODE)
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
            table_util.load_data_setting(self.start_num_lineEdit, Settings.INVOICE_START_NUM)
            table_util.load_data_setting(self.end_num_lineEdit, Settings.INVOICE_END_NUM)
            table_util.load_data_setting(self.temp_img_font_size_lineEdit, Settings.TEMP_FONT_SIZE)
            table_util.load_data_setting(self.temp_img_font_lineEdit, Settings.TEMP_FONT_NAME)
            table_util.load_data_setting(self.interface_input_lineEdit, Settings.INTERFACE_INPUT_PATH)
            table_util.load_data_setting(self.interface_output_lineEdit, Settings.INTERFACE_OUTPUT_PATH)
            table_util.load_data_setting(self.interface_temp_lineEdit, Settings.INTERFACE_TEMP_PATH)
            table_util.load_data_setting(self.beneficiary_lineEdit, Settings.BENEFICIARY_NAME)
            table_util.load_data_setting(self.reviewer_lineEdit, Settings.REVIEWER_NAME)
            table_util.load_data_setting(self.invoice_code_lineEdit, Settings.INVOICE_CODE)
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.exception(u"程序出现异常")
            logger.error(e)
