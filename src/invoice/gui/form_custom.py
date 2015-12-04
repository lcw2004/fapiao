# -*- coding: utf-8 -*-
import logging

from PyQt4.QtGui import QDialog

from form_custom_ui import *
from invoice.bean.beans import *
from invoice.common import common_util
from invoice.common import table_util


class CustomDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, custom_id=None):
        super(CustomDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.custom_id = custom_id

        # 初始化数据
        if custom_id:
            self.init_data(custom_id)

        # 绑定事件
        self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accepted)

    def accepted(self):
        """
        确定按钮事件
        :return:
        """
        try:
            code = table_util.get_edit_text(self.code_LineEdit)
            name = table_util.get_edit_text(self.name_LineEdit)
            tax_id = table_util.get_edit_text(self.tax_id_LineEdit)
            bank_account = table_util.get_edit_text(self.bank_account_LineEdit)
            addr = table_util.get_edit_text(self.addr_LineEdit)
            business_tax_id = table_util.get_edit_text(self.business_tax_id_LineEdit)
            erp_id = table_util.get_edit_text(self.erp_id_LineEdit)
            summary_title = table_util.get_edit_text(self.summary_title_LineEdit)
            remark = table_util.get_paint_context(self.remark_PlainTextEdit)

            if self.custom_id:
                # 修改
                q = Custom.update(code=code,
                                  name=name,
                                  tax_id=tax_id,
                                  bank_account=bank_account,
                                  addr=addr,
                                  business_tax_id=business_tax_id,
                                  erp_id=erp_id,
                                  summary_title=summary_title,
                                  remark=remark).where(Custom.id == self.custom_id)
                q.execute()
            else:
                # 添加
                custom = Custom.create(code=code,
                                       name=name,
                                       tax_id=tax_id,
                                       bank_account=bank_account,
                                       addr=addr,
                                       business_tax_id=business_tax_id,
                                       erp_id=erp_id,
                                       summary_title=summary_title,
                                       remark=remark)
                custom.save()

            # 刷新父窗体
            self.parent.custom_query_btn_clicked()
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.exception(u"报错客户信息出错！")
            logger.error(e)

    def init_data(self, custom_id):
        """
        根据客户ID，将客户的信息初始化到Dialog中
        :param custom_id:客户ID
        :return:
        """
        try:
            custom = Custom.get(id=custom_id)
            self.code_LineEdit.setText(common_util.to_string_trim(custom.code))
            self.name_LineEdit.setText(common_util.to_string_trim(custom.name))
            self.tax_id_LineEdit.setText(common_util.to_string_trim(custom.tax_id))
            self.bank_account_LineEdit.setText(common_util.to_string_trim(custom.bank_account))
            self.addr_LineEdit.setText(common_util.to_string_trim(custom.addr))
            self.business_tax_id_LineEdit.setText(common_util.to_string_trim(custom.business_tax_id))
            self.erp_id_LineEdit.setText(common_util.to_string_trim(custom.erp_id))
            self.summary_title_LineEdit.setText(common_util.to_string_trim(custom.summary_title))
            self.remark_PlainTextEdit.setPlainText(common_util.to_string_trim(custom.remark))
        except Custom.DoesNotExist:
            logger = logging.getLogger(__name__)
            logger.exception(u"程序出现异常")
