# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_section.ui'
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
        Dialog.resize(415, 173)
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
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 5)
        self.label_Number_2 = QtGui.QLabel(Dialog)
        self.label_Number_2.setObjectName(_fromUtf8("label_Number_2"))
        self.gridLayout.addWidget(self.label_Number_2, 0, 0, 1, 1)
        self.label_Number = QtGui.QLabel(Dialog)
        self.label_Number.setObjectName(_fromUtf8("label_Number"))
        self.gridLayout.addWidget(self.label_Number, 2, 0, 1, 1)
        self.label_Name = QtGui.QLabel(Dialog)
        self.label_Name.setObjectName(_fromUtf8("label_Name"))
        self.gridLayout.addWidget(self.label_Name, 1, 0, 1, 1)
        self.user_name_LineEdit = QtGui.QLineEdit(Dialog)
        self.user_name_LineEdit.setObjectName(_fromUtf8("user_name_LineEdit"))
        self.gridLayout.addWidget(self.user_name_LineEdit, 2, 2, 1, 1)
        self.end_num_LineEdit = QtGui.QLineEdit(Dialog)
        self.end_num_LineEdit.setObjectName(_fromUtf8("end_num_LineEdit"))
        self.gridLayout.addWidget(self.end_num_LineEdit, 1, 2, 1, 1)
        self.start_num_LineEdit = QtGui.QLineEdit(Dialog)
        self.start_num_LineEdit.setText(_fromUtf8(""))
        self.start_num_LineEdit.setObjectName(_fromUtf8("start_num_LineEdit"))
        self.gridLayout.addWidget(self.start_num_LineEdit, 0, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "编辑客户信息", None))
        self.label_Number_2.setText(_translate("Dialog", "号段起始值：", None))
        self.label_Number.setText(_translate("Dialog", "使用人姓名：", None))
        self.label_Name.setText(_translate("Dialog", "号段结束值：", None))
