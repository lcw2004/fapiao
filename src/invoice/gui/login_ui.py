# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogLogin(object):
    def setupUi(self, DialogLogin):
        DialogLogin.setObjectName(_fromUtf8("DialogLogin"))
        DialogLogin.resize(289, 229)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(DialogLogin)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelGGPOLogo = QtGui.QLabel(DialogLogin)
        self.labelGGPOLogo.setText(_fromUtf8(""))
        self.labelGGPOLogo.setPixmap(QtGui.QPixmap(_fromUtf8(":/assets/logo-vertical.png")))
        self.labelGGPOLogo.setObjectName(_fromUtf8("labelGGPOLogo"))
        self.horizontalLayout_2.addWidget(self.labelGGPOLogo)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.formLayout.setMargin(6)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.labelUsername = QtGui.QLabel(DialogLogin)
        self.labelUsername.setObjectName(_fromUtf8("labelUsername"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelUsername)
        self.login_username_edit = QtGui.QLineEdit(DialogLogin)
        self.login_username_edit.setObjectName(_fromUtf8("login_username_edit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.login_username_edit)
        self.labelPassword = QtGui.QLabel(DialogLogin)
        self.labelPassword.setObjectName(_fromUtf8("labelPassword"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelPassword)
        self.login_password_edit = QtGui.QLineEdit(DialogLogin)
        self.login_password_edit.setEchoMode(QtGui.QLineEdit.Password)
        self.login_password_edit.setObjectName(_fromUtf8("login_password_edit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.login_password_edit)
        self.login_save_password_chk = QtGui.QCheckBox(DialogLogin)
        self.login_save_password_chk.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_save_password_chk.setObjectName(_fromUtf8("login_save_password_chk"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.login_save_password_chk)
        self.login_auto_login_chk = QtGui.QCheckBox(DialogLogin)
        self.login_auto_login_chk.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_auto_login_chk.setObjectName(_fromUtf8("login_auto_login_chk"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.login_auto_login_chk)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.login_login_btn = QtGui.QPushButton(DialogLogin)
        self.login_login_btn.setObjectName(_fromUtf8("login_login_btn"))
        self.horizontalLayout.addWidget(self.login_login_btn)
        self.login_quit_btn = QtGui.QPushButton(DialogLogin)
        self.login_quit_btn.setObjectName(_fromUtf8("login_quit_btn"))
        self.horizontalLayout.addWidget(self.login_quit_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.login_error_label = QtGui.QLabel(DialogLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_error_label.sizePolicy().hasHeightForWidth())
        self.login_error_label.setSizePolicy(sizePolicy)
        self.login_error_label.setMouseTracking(False)
        self.login_error_label.setStyleSheet(_fromUtf8("QLabel { color : red; font-weight: bold}"))
        self.login_error_label.setText(_fromUtf8(""))
        self.login_error_label.setTextFormat(QtCore.Qt.PlainText)
        self.login_error_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.login_error_label.setWordWrap(True)
        self.login_error_label.setObjectName(_fromUtf8("login_error_label"))
        self.verticalLayout.addWidget(self.login_error_label)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.login_company_name_label = QtGui.QLabel(DialogLogin)
        self.login_company_name_label.setObjectName(_fromUtf8("login_company_name_label"))
        self.horizontalLayout_21.addWidget(self.login_company_name_label)
        self.login_product_name_label = QtGui.QLabel(DialogLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_product_name_label.sizePolicy().hasHeightForWidth())
        self.login_product_name_label.setSizePolicy(sizePolicy)
        self.login_product_name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_product_name_label.setObjectName(_fromUtf8("login_product_name_label"))
        self.horizontalLayout_21.addWidget(self.login_product_name_label)
        self.verticalLayout.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.labelUsername.setBuddy(self.login_username_edit)
        self.labelPassword.setBuddy(self.login_password_edit)

        self.retranslateUi(DialogLogin)
        QtCore.QMetaObject.connectSlotsByName(DialogLogin)
        DialogLogin.setTabOrder(self.login_username_edit, self.login_password_edit)
        DialogLogin.setTabOrder(self.login_password_edit, self.login_save_password_chk)
        DialogLogin.setTabOrder(self.login_save_password_chk, self.login_quit_btn)

    def retranslateUi(self, DialogLogin):
        DialogLogin.setWindowTitle(_translate("DialogLogin", "发票助手 V2.0", None))
        self.labelUsername.setText(_translate("DialogLogin", "用户名：", None))
        self.labelPassword.setText(_translate("DialogLogin", "密码：", None))
        self.login_save_password_chk.setText(_translate("DialogLogin", "保存密码", None))
        self.login_auto_login_chk.setText(_translate("DialogLogin", "自动登录", None))
        self.login_login_btn.setText(_translate("DialogLogin", "登录", None))
        self.login_quit_btn.setText(_translate("DialogLogin", "退出", None))
        self.login_company_name_label.setText(_translate("DialogLogin", "长沙瑞财科技有限公司", None))
        self.login_product_name_label.setText(_translate("DialogLogin", "发票助手 V2.0", None))

