# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_custom.ui'
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
        Dialog.resize(435, 392)
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
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_Number = QtGui.QLabel(Dialog)
        self.label_Number.setObjectName(_fromUtf8("label_Number"))
        self.gridLayout.addWidget(self.label_Number, 2, 0, 1, 1)
        self.label_Name = QtGui.QLabel(Dialog)
        self.label_Name.setObjectName(_fromUtf8("label_Name"))
        self.gridLayout.addWidget(self.label_Name, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 10, 0, 1, 5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 9, 3, 1, 1)
        self.label_Number_2 = QtGui.QLabel(Dialog)
        self.label_Number_2.setObjectName(_fromUtf8("label_Number_2"))
        self.gridLayout.addWidget(self.label_Number_2, 0, 0, 1, 1)
        self.label_Total = QtGui.QLabel(Dialog)
        self.label_Total.setObjectName(_fromUtf8("label_Total"))
        self.gridLayout.addWidget(self.label_Total, 3, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.name_LineEdit = QtGui.QLineEdit(Dialog)
        self.name_LineEdit.setObjectName(_fromUtf8("name_LineEdit"))
        self.gridLayout.addWidget(self.name_LineEdit, 1, 2, 1, 1)
        self.tax_id_LineEdit = QtGui.QLineEdit(Dialog)
        self.tax_id_LineEdit.setObjectName(_fromUtf8("tax_id_LineEdit"))
        self.gridLayout.addWidget(self.tax_id_LineEdit, 2, 2, 1, 1)
        self.addr_LineEdit = QtGui.QLineEdit(Dialog)
        self.addr_LineEdit.setObjectName(_fromUtf8("addr_LineEdit"))
        self.gridLayout.addWidget(self.addr_LineEdit, 4, 2, 1, 1)
        self.business_tax_id_LineEdit = QtGui.QLineEdit(Dialog)
        self.business_tax_id_LineEdit.setObjectName(_fromUtf8("business_tax_id_LineEdit"))
        self.gridLayout.addWidget(self.business_tax_id_LineEdit, 5, 2, 1, 1)
        self.erp_id_LineEdit = QtGui.QLineEdit(Dialog)
        self.erp_id_LineEdit.setObjectName(_fromUtf8("erp_id_LineEdit"))
        self.gridLayout.addWidget(self.erp_id_LineEdit, 6, 2, 1, 1)
        self.summary_title_LineEdit = QtGui.QLineEdit(Dialog)
        self.summary_title_LineEdit.setObjectName(_fromUtf8("summary_title_LineEdit"))
        self.gridLayout.addWidget(self.summary_title_LineEdit, 7, 2, 1, 1)
        self.bank_account_LineEdit = QtGui.QLineEdit(Dialog)
        self.bank_account_LineEdit.setObjectName(_fromUtf8("bank_account_LineEdit"))
        self.gridLayout.addWidget(self.bank_account_LineEdit, 3, 2, 1, 1)
        self.code_LineEdit = QtGui.QLineEdit(Dialog)
        self.code_LineEdit.setText(_fromUtf8(""))
        self.code_LineEdit.setObjectName(_fromUtf8("code_LineEdit"))
        self.gridLayout.addWidget(self.code_LineEdit, 0, 2, 1, 1)
        self.remark_PlainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.remark_PlainTextEdit.setLineWidth(0)
        self.remark_PlainTextEdit.setObjectName(_fromUtf8("remark_PlainTextEdit"))
        self.gridLayout.addWidget(self.remark_PlainTextEdit, 8, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "编辑客户信息", None))
        self.label.setText(_translate("Dialog", "客户地址：", None))
        self.label_Number.setText(_translate("Dialog", "客户税号：", None))
        self.label_Name.setText(_translate("Dialog", "客户名称：", None))
        self.label_Number_2.setText(_translate("Dialog", "客户代码：", None))
        self.label_Total.setText(_translate("Dialog", "开户银行账号：", None))
        self.label_4.setText(_translate("Dialog", "开票汇总名称：", None))
        self.label_5.setText(_translate("Dialog", "备注：", None))
        self.label_2.setText(_translate("Dialog", "企业税号：", None))
        self.label_3.setText(_translate("Dialog", "ERP对照值：", None))

