# -*- coding: utf-8 -*-
from PyQt4.QtGui import QDialog, QMessageBox
from menu_register_ui import *
from invoice.common.settings import Settings
import base64

class RegisterDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(RegisterDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        # 绑定事件
        self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accepted)

    def accepted(self):
        register_info = self.register_textEdit.toPlainText()
        try:
            register_info = base64.b64decode(register_info)
            if register_info == "this is develop by lcw":
                Settings.set_value(Settings.REGISTER_INFO, "True")
                QMessageBox.information(self.parentWidget(), "Information", u'注册成功！')
            else:
                QMessageBox.information(self.parentWidget(), "Information", u'注册失败！')
                return
        except Exception:
            QMessageBox.information(self.parentWidget(), "Information", u'注册失败！')