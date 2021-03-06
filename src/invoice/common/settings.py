# -*- coding: utf-8 -*-
import pickle
import os.path
import logging

from PyQt4.QtCore import QSettings

class Settings:

    logger = logging.getLogger(__name__)

    # ============ 登录配置 ============
    AUTO_LOGIN = 'auto_login'
    USER_ID = 'user_id'
    SAVE_PASSWORD = "save_password"
    LOGIN_NAME = 'login_name'
    PASSWORD = 'password'
    REGISTER_INFO = 'register_info'
    # ============ 登录配置 ============

    # ============ 模板配置 ============
    TEMP_FONT_NAME = "temp_font_name"
    TEMP_FONT_SIZE = "temp_font_size"
    # ============ 模板配置 ============

    # ============ 航空金税接口配置 ============
    INTERFACE_INPUT_PATH = "interface_input_path"
    INTERFACE_OUTPUT_PATH = "interface_output_path"
    INTERFACE_TEMP_PATH = "interface_temp_path"
    # ============ 航空金税接口配置 ============

    # ============ 模板配置 ============
    INVOICE_START_NUM = "invoice_start_num"
    INVOICE_END_NUM = "invoice_end_num"
    INVOICE_CURRENT_NUM = "invoice_current_num"
    # ============ 模板配置 ============

    # ============ 模板配置 ============
    BENEFICIARY_NAME = "beneficiary_name"
    REVIEWER_NAME = "reviewer_name"
    INVOICE_CODE = "invoice_code"
    # ============ 模板配置 ============

    _settings = QSettings(os.path.join(os.path.expanduser("~"), 'invoice_helper.ini'), QSettings.IniFormat)

    def __init__(self):
        pass

    @staticmethod
    def set_value(key, val):
        logging.info("Set:" + str(key) + " -> " + str(val))
        Settings._settings.setValue(key, val)

    @staticmethod
    def set_value_if_null(key, val):
        if not Settings.value_str(key):
            Settings.set_value(key, val)

    @staticmethod
    def value(key):
        val = Settings._settings.value(key)
        return val

    @staticmethod
    def value_str(key):
        return str(Settings.value_q_str(key))

    @staticmethod
    def value_q_str(key):
        value = Settings.value(key)
        if value.isNull():
            return ""
        else:
            return value.toString()

    @staticmethod
    def value_bool(key):
        value = Settings.value(key)
        if value.isNull():
            return False
        else:
            return value.toBool()

    @staticmethod
    def value_int(key):
        value = Settings.value(key)
        if value.isNull():
            return 0
        else:
            return value.toInt()[0]

    @staticmethod
    def value_long(key):
        value = Settings.value(key)
        if value.isNull():
            return 0
        else:
            return value.toInt()[0]

if __name__ == "__main__":
    print Settings.value_str(Settings.LOGIN_NAME), type(Settings.value_str(Settings.LOGIN_NAME))
    print Settings.value_int(Settings.INVOICE_START_NUM), type(Settings.value_int(Settings.INVOICE_START_NUM))
    print Settings.value_bool(Settings.AUTO_LOGIN), type(Settings.value_bool(Settings.AUTO_LOGIN))
    print Settings.value_long(Settings.INVOICE_END_NUM), type(Settings.value_long(Settings.INVOICE_END_NUM))
