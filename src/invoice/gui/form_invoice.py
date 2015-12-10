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
            invoice_num = table_util.get_edit_text(self.invoice_num_lineEdit)
            custom_name = table_util.get_edit_text(self.custom_name_lineEdit)
            total_num = table_util.get_edit_text(self.total_num_lineEdit)
            drawer = table_util.get_edit_text(self.drawer_lineEdit)
            beneficiary = table_util.get_edit_text(self.beneficiary_lineEdit)
            reviewer = table_util.get_edit_text(self.reviewer_lineEdit)

            # 保存用户信息
            try:
                custom_of_this = Custom.get(name=custom_name)
            except Exception:
                custom_of_this = Custom.create(name=custom_name)
                custom_of_this.save()

            if self.id:
                # 修改
                q = Invoice.update(invoice_num=invoice_num,
                                   total_num=total_num,
                                   drawer=drawer,
                                   beneficiary=beneficiary,
                                   reviewer=reviewer,
                                   custom=custom_of_this).where(Invoice.id == self.id)
                q.execute()
            else:
                # 添加
                invoice = Invoice.create(invoice_num=invoice_num,
                                         total_num=total_num,
                                         drawer=drawer,
                                         beneficiary=beneficiary,
                                         reviewer=reviewer,
                                         custom=custom_of_this)
                invoice.save()

            # 刷新父窗体
            self.parent.invoice_filter_btn_clicked()
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
