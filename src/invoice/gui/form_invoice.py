# -*- coding: utf-8 -*-
import logging

from PyQt4.QtGui import QDialog

from form_invoice_ui import *
from invoice.bean.beans import *
from invoice.common import common_util
from invoice.common import table_util
from invoice.common.settings import Settings
from invoice.image import image_util


class InvoiceDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, id=None):
        super(InvoiceDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.id = id

        # 初始化数据
        if id:
            self.init_data(id)
        else:
            self.init_default_data()

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

            if self.id:
                # 修改
                q = Custom.update(code=code,
                                  name=name,
                                  tax_id=tax_id,
                                  bank_account=bank_account,
                                  addr=addr,
                                  business_tax_id=business_tax_id,
                                  erp_id=erp_id,
                                  summary_title=summary_title,
                                  remark=remark).where(Custom.id == self.id)
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

    def init_default_data(self):
        # 将当前登录用户作为开票人
        user_id = Settings.value(Settings.USER_ID).toInt()[0]
        user = User.get(id=user_id)
        self.drawer_lineEdit.setText(user.name)



    def init_data(self, id):
        """
        根据发票ID，将发票的信息初始化到Dialog中
        :param id:客户ID
        :return:
        """
        try:
            # 设置发票信息
            invoice = Invoice.get(id=id)
            self.invoice_num_lineEdit.setText(common_util.to_string_trim(invoice.invoice_num))
            self.custom_name_lineEdit.setText(common_util.to_string_trim(invoice.custom.name))
            self.total_num_lineEdit.setText(common_util.to_string_trim(invoice.total_num))
            self.total_num_cn_lineEdit.setText(common_util.to_string_trim(invoice.total_num))
            self.drawer_lineEdit.setText(common_util.to_string_trim(invoice.drawer))
            self.beneficiary_lineEdit.setText(common_util.to_string_trim(invoice.beneficiary))
            self.reviewer_lineEdit.setText(common_util.to_string_trim(invoice.reviewer))

            # 根据ID查询明细
            invoice_detail_list = list(Invoice.get(id=id).invoiceDetails)
            row_count = len(invoice_detail_list)
            invoice_detail_table = self.invoice_detail_tableWidget
            invoice_detail_table.setRowCount(row_count)

            # 将数据加载到表格中
            for i in range(row_count):
                invoice_detail = invoice_detail_list[i]

                table_util.set_table_item_value(invoice_detail_table, i, 0, invoice_detail.id)
                table_util.set_table_item_value(invoice_detail_table, i, 1, invoice_detail.product.code)
                table_util.set_table_item_value(invoice_detail_table, i, 2, invoice_detail.product.name)
                table_util.set_table_item_value(invoice_detail_table, i, 3, invoice_detail.pro_num)
                table_util.set_table_item_value(invoice_detail_table, i, 4, invoice_detail.product.unit_price)
                table_util.set_table_item_value(invoice_detail_table, i, 5, invoice_detail.contain_tax_price)
        except Invoice.DoesNotExist:
            logger = logging.getLogger(__name__)
            logger.exception(u"程序出现异常")
