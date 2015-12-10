# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_config.ui'
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
        Dialog.resize(382, 333)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridGroupBox = QtGui.QGroupBox(Dialog)
        self.gridGroupBox.setObjectName(_fromUtf8("gridGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.gridGroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.start_num_lineEdit = QtGui.QLineEdit(self.gridGroupBox)
        self.start_num_lineEdit.setObjectName(_fromUtf8("start_num_lineEdit"))
        self.gridLayout.addWidget(self.start_num_lineEdit, 0, 1, 1, 1)
        self.end_num_lineEdit = QtGui.QLineEdit(self.gridGroupBox)
        self.end_num_lineEdit.setObjectName(_fromUtf8("end_num_lineEdit"))
        self.gridLayout.addWidget(self.end_num_lineEdit, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridGroupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridGroupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.gridGroupBox)
        self.gridGroupBox1 = QtGui.QGroupBox(Dialog)
        self.gridGroupBox1.setObjectName(_fromUtf8("gridGroupBox1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridGroupBox1)
        self.gridLayout_2.setContentsMargins(9, 9, -1, -1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.gridGroupBox1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridGroupBox1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.temp_img_font_ComboBox = QtGui.QFontComboBox(self.gridGroupBox1)
        self.temp_img_font_ComboBox.setObjectName(_fromUtf8("temp_img_font_ComboBox"))
        self.gridLayout_2.addWidget(self.temp_img_font_ComboBox, 0, 1, 1, 1)
        self.temp_img_font_size_lineEdit = QtGui.QLineEdit(self.gridGroupBox1)
        self.temp_img_font_size_lineEdit.setObjectName(_fromUtf8("temp_img_font_size_lineEdit"))
        self.gridLayout_2.addWidget(self.temp_img_font_size_lineEdit, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.gridGroupBox1)
        self.formGroupBox = QtGui.QGroupBox(Dialog)
        self.formGroupBox.setObjectName(_fromUtf8("formGroupBox"))
        self.formLayout = QtGui.QFormLayout(self.formGroupBox)
        self.formLayout.setContentsMargins(-1, 9, 9, -1)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_5 = QtGui.QLabel(self.formGroupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.formGroupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(self.formGroupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
        self.interface_input_lineEdit = QtGui.QLineEdit(self.formGroupBox)
        self.interface_input_lineEdit.setObjectName(_fromUtf8("interface_input_lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.interface_input_lineEdit)
        self.interface_output_lineEdit = QtGui.QLineEdit(self.formGroupBox)
        self.interface_output_lineEdit.setObjectName(_fromUtf8("interface_output_lineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.interface_output_lineEdit)
        self.interface_temp_lineEdit = QtGui.QLineEdit(self.formGroupBox)
        self.interface_temp_lineEdit.setObjectName(_fromUtf8("interface_temp_lineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.interface_temp_lineEdit)
        self.verticalLayout.addWidget(self.formGroupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.start_num_lineEdit, self.end_num_lineEdit)
        Dialog.setTabOrder(self.end_num_lineEdit, self.temp_img_font_ComboBox)
        Dialog.setTabOrder(self.temp_img_font_ComboBox, self.temp_img_font_size_lineEdit)
        Dialog.setTabOrder(self.temp_img_font_size_lineEdit, self.interface_input_lineEdit)
        Dialog.setTabOrder(self.interface_input_lineEdit, self.interface_output_lineEdit)
        Dialog.setTabOrder(self.interface_output_lineEdit, self.interface_temp_lineEdit)
        Dialog.setTabOrder(self.interface_temp_lineEdit, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "系统设置", None))
        self.gridGroupBox.setTitle(_translate("Dialog", "票段设置", None))
        self.label_2.setText(_translate("Dialog", "结束票号：", None))
        self.label.setText(_translate("Dialog", "起始票号：", None))
        self.gridGroupBox1.setTitle(_translate("Dialog", "发票模板", None))
        self.label_3.setText(_translate("Dialog", "字体名称：", None))
        self.label_4.setText(_translate("Dialog", "字体大小：", None))
        self.formGroupBox.setTitle(_translate("Dialog", "税控系统接口设置", None))
        self.label_5.setText(_translate("Dialog", "输入文件路径：", None))
        self.label_6.setText(_translate("Dialog", "输出文件路径：", None))
        self.label_7.setText(_translate("Dialog", "临时文件路径：", None))

