# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_invoice.ui'
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
        Dialog.resize(376, 188)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_Name = QtGui.QLabel(Dialog)
        self.label_Name.setObjectName(_fromUtf8("label_Name"))
        self.gridLayout.addWidget(self.label_Name, 1, 0, 1, 1)
        self.label_Number = QtGui.QLabel(Dialog)
        self.label_Number.setObjectName(_fromUtf8("label_Number"))
        self.gridLayout.addWidget(self.label_Number, 2, 0, 1, 1)
        self.label_UnitPrice = QtGui.QLabel(Dialog)
        self.label_UnitPrice.setObjectName(_fromUtf8("label_UnitPrice"))
        self.gridLayout.addWidget(self.label_UnitPrice, 2, 2, 1, 1)
        self.label_Date = QtGui.QLabel(Dialog)
        self.label_Date.setObjectName(_fromUtf8("label_Date"))
        self.gridLayout.addWidget(self.label_Date, 3, 2, 1, 1)
        self.dateEdit_Date = QtGui.QDateEdit(Dialog)
        self.dateEdit_Date.setCalendarPopup(True)
        self.dateEdit_Date.setObjectName(_fromUtf8("dateEdit_Date"))
        self.gridLayout.addWidget(self.dateEdit_Date, 3, 3, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 4)
        self.doubleSpinBox_InCome = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_InCome.setMinimum(-99999999.99)
        self.doubleSpinBox_InCome.setMaximum(99999999.99)
        self.doubleSpinBox_InCome.setObjectName(_fromUtf8("doubleSpinBox_InCome"))
        self.gridLayout.addWidget(self.doubleSpinBox_InCome, 2, 3, 1, 1)
        self.comboBox_Name = QtGui.QComboBox(Dialog)
        self.comboBox_Name.setEditable(True)
        self.comboBox_Name.setObjectName(_fromUtf8("comboBox_Name"))
        self.gridLayout.addWidget(self.comboBox_Name, 1, 1, 1, 1)
        self.label_Category = QtGui.QLabel(Dialog)
        self.label_Category.setObjectName(_fromUtf8("label_Category"))
        self.gridLayout.addWidget(self.label_Category, 1, 2, 1, 1)
        self.comboBox_Category = QtGui.QComboBox(Dialog)
        self.comboBox_Category.setEditable(True)
        self.comboBox_Category.setObjectName(_fromUtf8("comboBox_Category"))
        self.gridLayout.addWidget(self.comboBox_Category, 1, 3, 1, 1)
        self.doubleSpinBox_OutCome = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_OutCome.setMinimum(-99999999.99)
        self.doubleSpinBox_OutCome.setMaximum(99999999.99)
        self.doubleSpinBox_OutCome.setObjectName(_fromUtf8("doubleSpinBox_OutCome"))
        self.gridLayout.addWidget(self.doubleSpinBox_OutCome, 2, 1, 1, 1)
        self.label_Total = QtGui.QLabel(Dialog)
        self.label_Total.setObjectName(_fromUtf8("label_Total"))
        self.gridLayout.addWidget(self.label_Total, 3, 0, 1, 1)
        self.doubleSpinBox_Total = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_Total.setMinimum(-99999999.99)
        self.doubleSpinBox_Total.setMaximum(99999999.99)
        self.doubleSpinBox_Total.setObjectName(_fromUtf8("doubleSpinBox_Total"))
        self.gridLayout.addWidget(self.doubleSpinBox_Total, 3, 1, 1, 1)
        self.label_Number_2 = QtGui.QLabel(Dialog)
        self.label_Number_2.setObjectName(_fromUtf8("label_Number_2"))
        self.gridLayout.addWidget(self.label_Number_2, 0, 0, 1, 1)
        self.spinBox_Number = QtGui.QSpinBox(Dialog)
        self.spinBox_Number.setMinimum(1)
        self.spinBox_Number.setMaximum(99999999)
        self.spinBox_Number.setObjectName(_fromUtf8("spinBox_Number"))
        self.gridLayout.addWidget(self.spinBox_Number, 0, 1, 1, 1)
        self.label_Name.setBuddy(self.comboBox_Name)
        self.label_Number.setBuddy(self.doubleSpinBox_OutCome)
        self.label_UnitPrice.setBuddy(self.doubleSpinBox_InCome)
        self.label_Date.setBuddy(self.dateEdit_Date)
        self.label_Category.setBuddy(self.comboBox_Category)
        self.label_Total.setBuddy(self.doubleSpinBox_Total)
        self.label_Number_2.setBuddy(self.spinBox_Number)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboBox_Name, self.comboBox_Category)
        Dialog.setTabOrder(self.comboBox_Category, self.doubleSpinBox_OutCome)
        Dialog.setTabOrder(self.doubleSpinBox_OutCome, self.doubleSpinBox_InCome)
        Dialog.setTabOrder(self.doubleSpinBox_InCome, self.doubleSpinBox_Total)
        Dialog.setTabOrder(self.doubleSpinBox_Total, self.dateEdit_Date)
        Dialog.setTabOrder(self.dateEdit_Date, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "编辑", None))
        self.label_Name.setText(_translate("Dialog", "品名(&N)：", None))
        self.label_Number.setText(_translate("Dialog", "出账(&U)：", None))
        self.label_UnitPrice.setText(_translate("Dialog", "入账(&I)：", None))
        self.label_Date.setText(_translate("Dialog", "日期(&D)：", None))
        self.dateEdit_Date.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd", None))
        self.label_Category.setText(_translate("Dialog", "类别(&C)：", None))
        self.label_Total.setText(_translate("Dialog", "余额(&T)：", None))
        self.label_Number_2.setText(_translate("Dialog", "编号(&I)", None))

import pygrid_rc
