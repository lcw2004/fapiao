# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(577, 489)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Administrator/.designer/backup/image/main_logo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setMargin(11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_0 = QtGui.QWidget()
        self.tab_0.setStyleSheet(_fromUtf8(""))
        self.tab_0.setObjectName(_fromUtf8("tab_0"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_0)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(3)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.selectAllButton = QtGui.QPushButton(self.tab_0)
        self.selectAllButton.setInputMethodHints(QtCore.Qt.ImhNone)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Administrator/.designer/backup/image/op_select_all.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectAllButton.setIcon(icon1)
        self.selectAllButton.setIconSize(QtCore.QSize(16, 16))
        self.selectAllButton.setAutoRepeat(False)
        self.selectAllButton.setObjectName(_fromUtf8("selectAllButton"))
        self.horizontalLayout.addWidget(self.selectAllButton)
        self.filterButton = QtGui.QPushButton(self.tab_0)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Administrator/.designer/backup/image/op_filter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filterButton.setIcon(icon2)
        self.filterButton.setObjectName(_fromUtf8("filterButton"))
        self.horizontalLayout.addWidget(self.filterButton)
        self.genInvoiceButton = QtGui.QPushButton(self.tab_0)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Administrator/.designer/backup/image/op_gen_invoince.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genInvoiceButton.setIcon(icon3)
        self.genInvoiceButton.setObjectName(_fromUtf8("genInvoiceButton"))
        self.horizontalLayout.addWidget(self.genInvoiceButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setMargin(3)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.tab_0)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.excelFilePathEdit = QtGui.QLineEdit(self.tab_0)
        self.excelFilePathEdit.setObjectName(_fromUtf8("excelFilePathEdit"))
        self.horizontalLayout_2.addWidget(self.excelFilePathEdit)
        self.selectExcelFileButton = QtGui.QPushButton(self.tab_0)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Administrator/.designer/backup/image/excel.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectExcelFileButton.setIcon(icon4)
        self.selectExcelFileButton.setObjectName(_fromUtf8("selectExcelFileButton"))
        self.horizontalLayout_2.addWidget(self.selectExcelFileButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.excelTableWidget = QtGui.QTableWidget(self.tab_0)
        self.excelTableWidget.setRowCount(0)
        self.excelTableWidget.setColumnCount(0)
        self.excelTableWidget.setObjectName(_fromUtf8("excelTableWidget"))
        self.verticalLayout.addWidget(self.excelTableWidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Administrator/.designer/backup/image/tab_import.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_0, icon5, _fromUtf8(""))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_1)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setMargin(3)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.invoice_filter_Button = QtGui.QPushButton(self.tab_1)
        self.invoice_filter_Button.setObjectName(_fromUtf8("invoice_filter_Button"))
        self.horizontalLayout_3.addWidget(self.invoice_filter_Button)
        self.invoince_update_btn = QtGui.QPushButton(self.tab_1)
        self.invoince_update_btn.setObjectName(_fromUtf8("invoince_update_btn"))
        self.horizontalLayout_3.addWidget(self.invoince_update_btn)
        self.invoince_delete_btn = QtGui.QPushButton(self.tab_1)
        self.invoince_delete_btn.setObjectName(_fromUtf8("invoince_delete_btn"))
        self.horizontalLayout_3.addWidget(self.invoince_delete_btn)
        self.invoince_import_xml_btn = QtGui.QPushButton(self.tab_1)
        self.invoince_import_xml_btn.setObjectName(_fromUtf8("invoince_import_xml_btn"))
        self.horizontalLayout_3.addWidget(self.invoince_import_xml_btn)
        self.invoince_merge_btn = QtGui.QPushButton(self.tab_1)
        self.invoince_merge_btn.setObjectName(_fromUtf8("invoince_merge_btn"))
        self.horizontalLayout_3.addWidget(self.invoince_merge_btn)
        self.invoince_chaifeng_btn = QtGui.QPushButton(self.tab_1)
        self.invoince_chaifeng_btn.setObjectName(_fromUtf8("invoince_chaifeng_btn"))
        self.horizontalLayout_3.addWidget(self.invoince_chaifeng_btn)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.invoiceTableWidget = QtGui.QTableWidget(self.tab_1)
        self.invoiceTableWidget.setRowCount(0)
        self.invoiceTableWidget.setColumnCount(14)
        self.invoiceTableWidget.setObjectName(_fromUtf8("invoiceTableWidget"))
        item = QtGui.QTableWidgetItem()
        self.invoiceTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.invoiceTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.invoiceTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.invoiceTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.invoiceTableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.invoiceTableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.invoiceTableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.invoiceTableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.invoiceTableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.invoiceTableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.invoiceTableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.invoiceTableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.invoiceTableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.invoiceTableWidget.setHorizontalHeaderItem(13, item)
        self.verticalLayout_4.addWidget(self.invoiceTableWidget)
        self.invoinceDetailTableWidget = QtGui.QTableWidget(self.tab_1)
        self.invoinceDetailTableWidget.setRowCount(0)
        self.invoinceDetailTableWidget.setColumnCount(10)
        self.invoinceDetailTableWidget.setObjectName(_fromUtf8("invoinceDetailTableWidget"))
        item = QtGui.QTableWidgetItem()
        self.invoinceDetailTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.invoinceDetailTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.invoinceDetailTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.invoinceDetailTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.invoinceDetailTableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.invoinceDetailTableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.invoinceDetailTableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.invoinceDetailTableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.invoinceDetailTableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.invoinceDetailTableWidget.setHorizontalHeaderItem(9, item)
        self.verticalLayout_4.addWidget(self.invoinceDetailTableWidget)
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setMargin(3)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.custom_add_btn = QtGui.QPushButton(self.tab_3)
        self.custom_add_btn.setObjectName(_fromUtf8("custom_add_btn"))
        self.horizontalLayout_4.addWidget(self.custom_add_btn)
        self.custom_update_btn = QtGui.QPushButton(self.tab_3)
        self.custom_update_btn.setObjectName(_fromUtf8("custom_update_btn"))
        self.horizontalLayout_4.addWidget(self.custom_update_btn)
        self.custom_delete_btn = QtGui.QPushButton(self.tab_3)
        self.custom_delete_btn.setObjectName(_fromUtf8("custom_delete_btn"))
        self.horizontalLayout_4.addWidget(self.custom_delete_btn)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.customTableWidget = QtGui.QTableWidget(self.tab_3)
        self.customTableWidget.setObjectName(_fromUtf8("customTableWidget"))
        self.customTableWidget.setColumnCount(0)
        self.customTableWidget.setRowCount(0)
        self.verticalLayout_9.addWidget(self.customTableWidget)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_11.setMargin(0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setMargin(3)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.product_add_btn = QtGui.QPushButton(self.tab_4)
        self.product_add_btn.setObjectName(_fromUtf8("product_add_btn"))
        self.horizontalLayout_6.addWidget(self.product_add_btn)
        self.product_update_btn = QtGui.QPushButton(self.tab_4)
        self.product_update_btn.setObjectName(_fromUtf8("product_update_btn"))
        self.horizontalLayout_6.addWidget(self.product_update_btn)
        self.product_delete_btn = QtGui.QPushButton(self.tab_4)
        self.product_delete_btn.setObjectName(_fromUtf8("product_delete_btn"))
        self.horizontalLayout_6.addWidget(self.product_delete_btn)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.productTableWidget = QtGui.QTableWidget(self.tab_4)
        self.productTableWidget.setObjectName(_fromUtf8("productTableWidget"))
        self.productTableWidget.setColumnCount(0)
        self.productTableWidget.setRowCount(0)
        self.verticalLayout_11.addWidget(self.productTableWidget)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 577, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menu_file = QtGui.QMenu(self.menuBar)
        self.menu_file.setObjectName(_fromUtf8("menu_file"))
        self.menu_config = QtGui.QMenu(self.menuBar)
        self.menu_config.setObjectName(_fromUtf8("menu_config"))
        self.menu_help = QtGui.QMenu(self.menuBar)
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.menu_file.addAction(self.actionOpen)
        self.menu_file.addAction(self.actionClose)
        self.menuBar.addAction(self.menu_file.menuAction())
        self.menuBar.addAction(self.menu_config.menuAction())
        self.menuBar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "发票开具系统", None))
        self.selectAllButton.setText(_translate("MainWindow", "全选", None))
        self.filterButton.setText(_translate("MainWindow", "筛选", None))
        self.genInvoiceButton.setText(_translate("MainWindow", "生成发票", None))
        self.label.setText(_translate("MainWindow", "文件", None))
        self.selectExcelFileButton.setText(_translate("MainWindow", "选择", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_0), _translate("MainWindow", "数据导入", None))
        self.invoice_filter_Button.setText(_translate("MainWindow", "查询", None))
        self.invoince_update_btn.setText(_translate("MainWindow", "修改", None))
        self.invoince_delete_btn.setText(_translate("MainWindow", "删除", None))
        self.invoince_import_xml_btn.setText(_translate("MainWindow", "导入到开票系统", None))
        self.invoince_merge_btn.setText(_translate("MainWindow", "合并", None))
        self.invoince_chaifeng_btn.setText(_translate("MainWindow", "拆分", None))
        item = self.invoiceTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID", None))
        item = self.invoiceTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "发票号码", None))
        item = self.invoiceTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "客户名称", None))
        item = self.invoiceTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "总不含税金额", None))
        item = self.invoiceTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "总金额", None))
        item = self.invoiceTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "价税合计", None))
        item = self.invoiceTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "系统流水号", None))
        item = self.invoiceTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "客户代码", None))
        item = self.invoiceTableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "客户税号", None))
        item = self.invoiceTableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "客户地址", None))
        item = self.invoiceTableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "客户开户行账号", None))
        item = self.invoiceTableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "备注", None))
        item = self.invoiceTableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "开票人", None))
        item = self.invoiceTableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "收款人", None))
        item = self.invoinceDetailTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID", None))
        item = self.invoinceDetailTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "产品代码", None))
        item = self.invoinceDetailTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "产品名称", None))
        item = self.invoinceDetailTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "产品型号", None))
        item = self.invoinceDetailTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "产品单位", None))
        item = self.invoinceDetailTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "产品单价", None))
        item = self.invoinceDetailTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "产品数量", None))
        item = self.invoinceDetailTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "含税单价", None))
        item = self.invoinceDetailTableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "税率", None))
        item = self.invoinceDetailTableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "税额", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "临时待处理数据", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "已开发票", None))
        self.custom_add_btn.setText(_translate("MainWindow", "新增", None))
        self.custom_update_btn.setText(_translate("MainWindow", "修改", None))
        self.custom_delete_btn.setText(_translate("MainWindow", "删除", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "客户管理", None))
        self.product_add_btn.setText(_translate("MainWindow", "新增", None))
        self.product_update_btn.setText(_translate("MainWindow", "修改", None))
        self.product_delete_btn.setText(_translate("MainWindow", "删除", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "商品管理", None))
        self.menu_file.setTitle(_translate("MainWindow", "文件", None))
        self.menu_config.setTitle(_translate("MainWindow", "配置", None))
        self.menu_help.setTitle(_translate("MainWindow", "帮助", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionOpen.setText(_translate("MainWindow", "打开", None))
        self.actionClose.setText(_translate("MainWindow", "关闭", None))

