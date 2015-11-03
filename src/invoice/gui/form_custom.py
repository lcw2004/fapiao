# -*- coding: utf-8 -*-
import logging
from PyQt4.QtGui import QDialog

from form_custom_ui import *
from invoice.bean.beans import *
from invoice.common import table_util
from invoice.common import common_util

class CustomDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, custom_id=None):
        super(CustomDialog, self).__init__(parent)
        self.setupUi(self)

        # 初始化数据
        if custom_id:
            self.custom_id = custom_id
            self.init_data(custom_id)

    def init_data(self, custom_id):
        try:
            custom = Custom.get(id=custom_id)
            self.code_LineEdit.setText(common_util.to_string_trim(custom.code))
            self.name_LineEdit.setText(common_util.to_string_trim(custom.name))
            self.tax_id_LineEdit.setText(common_util.to_string_trim(custom.tax_id))
            self.bank_account_LineEdit.setText(common_util.to_string_trim(custom.bank_account))
            self.addr_LineEdit.setText(common_util.to_string_trim(custom.addr))
            self.business_tax_id_LineEdit.setText(common_util.to_string_trim(custom.business_tax_di))
            self.erp_id_LineEdit.setText(common_util.to_string_trim(custom.erp_id))
            self.summary_title_LineEdit.setText(common_util.to_string_trim(custom.summary_title))
            self.remark_PlainTextEdit.setPlainText(common_util.to_string_trim(custom.remark))
        except Custom.DoesNotExist:
            logger = logging.getLogger(__name__)
            logger.exception(u"程序出现异常")


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = CustomDialog(2)
    dialog.show()
    sys.exit(app.exec_())