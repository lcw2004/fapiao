# -*- coding: utf-8 -*-
import logging
from PyQt4 import QtCore
from PyQt4.QtGui import QDialog

from invoice.bean.beans import User
from invoice.common import table_util
from invoice.common.settings import Settings
from invoice.gui.login_ui import Ui_DialogLogin

logger = logging.getLogger(__name__)


class LoginDialog(QDialog, Ui_DialogLogin):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.setupUi(self)
        self.init_from_setting()

        self.connect(self.login_login_btn, QtCore.SIGNAL("clicked()"), self.login_login_btn_clicked)
        self.connect(self.login_quit_btn, QtCore.SIGNAL("clicked()"), self.login_quit_btn_clicked)

    def init_from_setting(self):
        logger.info(u"从Setting中加载配置")
        if Settings.value(Settings.SAVE_PASSWORD).toBool():
            self.login_save_password_chk.setChecked(True)
        if Settings.value(Settings.AUTO_LOGIN).toBool():
            self.login_auto_login_chk.setChecked(True)

        login_name = Settings.value(Settings.LOGIN_NAME).toString()
        password = Settings.value(Settings.PASSWORD).toString()
        self.login_username_edit.setText(login_name)
        self.login_password_edit.setText(password)

    def login_login_btn_clicked(self):
        login_name = table_util.get_edit_text(self.login_username_edit)
        password = table_util.get_edit_text(self.login_password_edit)

        # 判断登录名密码是否为空
        if not login_name:
            self.login_error_label.setText("请输入用户登录名！")
            return
        if not password:
            self.login_error_label.setText("请输入用户密码！")
            return

        # 判断是否需要保存密码
        if self.login_save_password_chk.isChecked():
            Settings.set_value(Settings.LOGIN_NAME, login_name)
            Settings.set_value(Settings.PASSWORD, password)
        else:
            Settings.set_value(Settings.LOGIN_NAME, '')
            Settings.set_value(Settings.PASSWORD, '')
        Settings.set_value(Settings.AUTO_LOGIN, self.login_auto_login_chk.isChecked())
        Settings.set_value(Settings.SAVE_PASSWORD, self.login_save_password_chk.isChecked())


        self.accept()

    def login_quit_btn_clicked(self):
        pass
