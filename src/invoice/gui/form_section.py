# -*- coding: utf-8 -*-
import logging
from PyQt4.QtGui import QDialog
from form_section_ui import *
from invoice.bean.beans import *
from invoice.common import common_util
from invoice.common import table_util


class SectionDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, id=None):
        super(SectionDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.id = id

        # 初始化数据
        if id:
            self.init_data(id)

        # 绑定事件
        self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accepted)

    def accepted(self):
        """
        确定按钮事件
        :return:
        """
        try:
            start_num = table_util.get_edit_text(self.start_num_LineEdit)
            end_num = table_util.get_edit_text(self.end_num_LineEdit)
            user_name = table_util.get_edit_text(self.user_name_LineEdit)

            if self.id:
                # 修改
                q = NoSection.update(start_num=start_num,
                                     end_num=end_num,
                                     user_name=user_name
                                     ).where(NoSection.id == self.id)
                q.execute()
            else:
                # 添加
                no_section = NoSection.create(start_num=start_num,
                                             end_num=end_num,
                                             user_name=user_name)
                no_section.save()

            # 刷新父窗体
            self.parent.section_query_btn_clicked()
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.exception(u"报错客户信息出错！")
            logger.error(e)

    def init_data(self, id):
        """
        根据客户ID，将客户的信息初始化到Dialog中
        :param id:客户ID
        :return:
        """
        try:
            no_section = NoSection.get(id=id)
            self.start_num_LineEdit.setText(common_util.to_string_trim(no_section.start_num))
            self.end_num_LineEdit.setText(common_util.to_string_trim(no_section.end_num))
            self.user_name_LineEdit.setText(common_util.to_string_trim(no_section.user_name))
        except NoSection.DoesNotExist:
            logger = logging.getLogger(__name__)
            logger.exception(u"程序出现异常")
