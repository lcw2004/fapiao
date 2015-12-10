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
        logging.info("Get:" + str(key) + " -> " + str(val))
        return val

    @staticmethod
    def value_str(key):
        return str(Settings.value(key).toString())

    @staticmethod
    def value_bool(key):
        return bool(Settings.value_str(key))

    @staticmethod
    def value_int(key):
        return int(Settings.value_str(key))
