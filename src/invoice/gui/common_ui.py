# -*- coding: utf-8 -*-
from PyQt4.QtGui import QItemDelegate, QTableView, QAbstractItemView, QComboBox
from invoice.common import table_util


class DBComboBoxDelegate(QItemDelegate):
    """
    下拉框表格
    """
    def __init__(self, combo_model, parent=None):
        QItemDelegate.__init__(self, parent)
        self.combo_model = combo_model
        self.parent = parent

    def create_table_view(self, parent):
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
        combo_box = QComboBox(parent)
        combo_box.setModel(self.combo_model)
        combo_box.setView(self.create_table_view(parent))
        return combo_box

    def setEditorData(self, editor, index):
        value = index.model().data(index).toString()
        editor.setCurrentIndex(editor.findText(value))

    def setModelData(self, editor, model, index):
        if editor.currentIndex() >= 0:
            real_index = editor.model().index(editor.currentIndex(), 1)
            value = editor.model().data(real_index)
            model.setData(index, value)

