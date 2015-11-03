# -*- coding: utf-8 -*-
import logging
from PyQt4.QtGui import QDialog

from form_custom_ui import *
from invoice.bean.beans import *

class CustomDialog(QDialog, Ui_Dialog):
    def __init__(self, custom_id=None):
        super(CustomDialog, self).__init__(None)
        self.setupUi(self)

        # 初始化数据
        if custom_id:
            self.custom_id = custom_id
            self.init_data(custom_id)

    def init_data(self, custom_id):
        try:
            custom = Custom.get(id=custom_id)
            self.code_LineEdit.setText(custom.code)
            self.name_LineEdit.setText(custom.name)
            self.tax_id_LineEdit.setText(custom.tax_id)
            self.bank_account_LineEdit.setText(custom.bank_account)
            self.addr_LineEdit.setText(custom.addr)
            self.business_tax_id_LineEdit.setText(custom.business_tax_di)
            self.erp_id_LineEdit.setText(custom.erp_id)
            self.summary_title_LineEdit.setText(custom.summary_title)
            self.remark_PlainTextEdit.setPlainText(custom.remark)
        except Custom.DoesNotExist:
            logger = logging.getLogger(__name__)
            logger.exception(u"程序出现异常")


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = CustomDialog(2)
    dialog.show()
    sys.exit(app.exec_())