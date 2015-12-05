# -*- coding: utf-8 -*-
import pickle
import os.path

from PyQt4.QtCore import QSettings

class Settings:
    AUTO_LOGIN = 'auto_login'
    USER_ID = 'user_id'
    SAVE_PASSWORD = "save_password"
    LOGIN_NAME = 'login_name'
    PASSWORD = 'password'

    _settings = QSettings(os.path.join(os.path.expanduser("~"), 'invoice_helper.ini'), QSettings.IniFormat)

    @staticmethod
    def set_boolean(key, val):
        if val:
            val = '1'
        else:
            val = ''
        Settings._settings.setValue(key, val)

    @staticmethod
    def set_python_value(key, val):
        try:
            Settings._settings.setValue(key, pickle.dumps(val))
        except pickle.PickleError:
            pass

    @staticmethod
    def python_value(key):
        try:
            return pickle.loads(Settings._settings.value(key))
        except:
            return None

    @staticmethod
    def set_value(key, val):
        Settings._settings.setValue(key, val)

    @staticmethod
    def value(key):
        return Settings._settings.value(key)
