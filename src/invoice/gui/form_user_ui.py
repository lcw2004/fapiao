# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_user.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(351, 200)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(25, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.login_name_lineEdit = QtGui.QLineEdit(Dialog)
        self.login_name_lineEdit.setObjectName(_fromUtf8("login_name_lineEdit"))
        self.gridLayout.addWidget(self.login_name_lineEdit, 1, 2, 1, 1)
        self.name_lineEdit = QtGui.QLineEdit(Dialog)
        self.name_lineEdit.setObjectName(_fromUtf8("name_lineEdit"))
        self.gridLayout.addWidget(self.name_lineEdit, 0, 2, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 5)
        self.label_Number_2 = QtGui.QLabel(Dialog)
        self.label_Number_2.setObjectName(_fromUtf8("label_Number_2"))
        self.gridLayout.addWidget(self.label_Number_2, 0, 0, 1, 1)
        self.label_Number = QtGui.QLabel(Dialog)
        self.label_Number.setObjectName(_fromUtf8("label_Number"))
        self.gridLayout.addWidget(self.label_Number, 2, 0, 1, 1)
        self.label_Name = QtGui.QLabel(Dialog)
        self.label_Name.setObjectName(_fromUtf8("label_Name"))
        self.gridLayout.addWidget(self.label_Name, 1, 0, 1, 1)
        self.is_admin_checkBox = QtGui.QCheckBox(Dialog)
        self.is_admin_checkBox.setObjectName(_fromUtf8("is_admin_checkBox"))
        self.gridLayout.addWidget(self.is_admin_checkBox, 4, 2, 1, 1)
        self.password_lineEdit = QtGui.QLineEdit(Dialog)
        self.password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        self.gridLayout.addWidget(self.password_lineEdit, 2, 2, 1, 1)
        self.password_again_lineEdit = QtGui.QLineEdit(Dialog)
        self.password_again_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.password_again_lineEdit.setObjectName(_fromUtf8("password_again_lineEdit"))
        self.gridLayout.addWidget(self.password_again_lineEdit, 3, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.name_lineEdit, self.login_name_lineEdit)
        Dialog.setTabOrder(self.login_name_lineEdit, self.password_lineEdit)
        Dialog.setTabOrder(self.password_lineEdit, self.password_again_lineEdit)
        Dialog.setTabOrder(self.password_again_lineEdit, self.is_admin_checkBox)
        Dialog.setTabOrder(self.is_admin_checkBox, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "编辑用户信息", None))
        self.label.setText(_translate("Dialog", "确认密码：", None))
        self.label_2.setText(_translate("Dialog", "是否是管理员：", None))
        self.label_Number_2.setText(_translate("Dialog", "姓名：", None))
        self.label_Number.setText(_translate("Dialog", "密码：", None))
        self.label_Name.setText(_translate("Dialog", "登录名：", None))
        self.is_admin_checkBox.setText(_translate("Dialog", "此选项用于控制是否能添加用户", None))

