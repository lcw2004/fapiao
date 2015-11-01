# -*- coding: utf-8 -*-
from PyQt4.QtGui import QDialog

from form_invoice_ui import *


class FormInvoiceDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(FormInvoiceDialog, self).__init__(parent)
        self.setupUi(self)