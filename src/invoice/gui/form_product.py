# -*- coding: utf-8 -*-
import logging

from PyQt4.QtGui import QDialog

from invoice.gui.form_product_ui import Ui_Dialog
from invoice.bean.beans import *
from invoice.common import common_util
from invoice.common import table_util

class ProductDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, product_id=None):
        super(ProductDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.product_id = product_id

        # 初始化数据
        if product_id:
            self.init_data(product_id)

        # 绑定事件
        # self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accepted)

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

    def init_data(self, product_id):
        """
        根据产品ID，将客户的信息初始化到Dialog中
        :param product_id:客户ID
        :return:
        """
        try:
            product = Product.get(id=product_id)
            self.code_LineEdit.setText(common_util.to_string_trim(product.code))
            self.name_LineEdit.setText(common_util.to_string_trim(product.name))
            self.type_LineEdit.setText(common_util.to_string_trim(product.type))
            self.unit_LineEdit.setText(common_util.to_string_trim(product.unit))
            self.unit_price_LineEdit.setText(common_util.to_string_trim(product.unit_price))
            self.tax_price_LineEdit.setText(common_util.to_string_trim(product.tax_price))
            self.tax_LineEdit.setText(common_util.to_string_trim(product.tax))
            self.business_tax_num_LineEdit.setText(common_util.to_string_trim(product.business_tax_num))
            self.erp_id_LineEdit.setText(common_util.to_string_trim(product.erp_id))
            self.p_id_LineEdit.setText(common_util.to_string_trim(product.p_id))
        except Product.DoesNotExist:
            logger = logging.getLogger(__name__)
            logger.exception(u"程序出现异常")