# -*- coding: utf-8 -*-
import logging

from PyQt4 import QtCore
from PyQt4.QtGui import QDialog

from invoice.gui.login_ui import Ui_DialogLogin

logger = logging.getLogger(__name__)


class LoginDialog(QDialog, Ui_DialogLogin):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.login_login_btn, QtCore.SIGNAL("clicked()"), self.login_login_btn_clicked)
        self.connect(self.login_quit_btn, QtCore.SIGNAL("clicked()"), self.login_quit_btn_clicked)

    def login_login_btn_clicked(self):
        self.accept();



    def login_quit_btn_clicked(self):
        pass

