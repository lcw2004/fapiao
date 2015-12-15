# -*- coding: utf-8 -*-
from PyQt4.QtCore import QModelIndex, QVariant
from PyQt4.QtGui import QItemDelegate, QTableView, QAbstractItemView, QComboBox, QStandardItemModel

from invoice.bean.beans import Product


class MyComboBox(QItemDelegate):
    def __init__(self, parent=None):
        QItemDelegate.__init__(self, parent)
        self.parent = parent

    def createEditor(self, parent, option, index):
        """
        重写父类的方法
        """
        print "---------------------"
        print "createEditor"
        combo_box = QComboBox(parent)
        combo_box.setEditable(True)

        # 将数据加载到表格中
        product_list = list(Product.select().where(Product.status == 0 and Product.name.is_null(False)))
        for product in product_list:
            combo_box.addItem(product.name)

        combo_box.editTextChanged.connect(self.editTextChanged)
        print "---------------------"
        return combo_box

class DBComboBoxDelegate(QItemDelegate):
    """
    下拉框表格
    """
    def __init__(self, parent=None):
        QItemDelegate.__init__(self, parent)
        self.parent = parent
        self.combo_model = self.crete_combo_model()
        self.combo_box = None

    def crete_combo_model(self):
        """
        创建Model
        """
        product_list = list(Product.select().where(Product.status == 0))
        row_count = len(product_list)

        combo_model = QStandardItemModel(4, 3, self)
        combo_model.setHorizontalHeaderLabels([u'名称', u'ID', u'单价'])
        combo_model.setRowCount(row_count)

        # 将数据加载到表格中
        for i in range(row_count):
            product = product_list[i]
            combo_model.setData(combo_model.index(i, 0, QModelIndex()), QVariant(product.name))
            combo_model.setData(combo_model.index(i, 1, QModelIndex()), QVariant(product.id))
            combo_model.setData(combo_model.index(i, 2, QModelIndex()), QVariant(product.unit_price))
        return combo_model

    def create_table_view(self, parent):
        """
        创建表格
        """
        view = QTableView(parent)
        view.setModel(self.combo_model)
        view.setAutoScroll(False)
        view.setSelectionMode(QAbstractItemView.SingleSelection)
        view.setSelectionBehavior(QAbstractItemView.SelectRows)
        view.resizeColumnsToContents()
        view.resizeRowsToContents()
        view.setMinimumWidth(view.horizontalHeader().length())
        return view

    def createEditor(self, parent, option, index):
        """
        重写父类的方法
        """
        combo_box = QComboBox(parent)
        combo_box.setEditable(True)
        combo_box.setModel(self.combo_model)
        combo_box.setView(self.create_table_view(parent))
        combo_box.editTextChanged.connect(self.editTextChanged)
        self.combo_box = combo_box
        return combo_box

    def setEditorData(self, editor, index):
        """
         重写父类的方法
         """
        value = index.model().data(index).toString()
        editor.setCurrentIndex(editor.findText(value))

    def setModelData(self, editor, model, index):
        """
         重写父类的方法
         """
        if editor.currentIndex() >= 0:
            real_index = editor.model().index(editor.currentIndex(), 1)
            value = editor.model().data(real_index)
            model.setData(index, value)

    def editTextChanged(self):
        print "editTextChanged", self.combo_box.currentText()