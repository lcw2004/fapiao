# -*- coding: utf-8 -*-
import logging
from PyQt4.QtGui import QDialog, QMessageBox
from form_user_ui import *
from invoice.bean.beans import *
from invoice.common import common_util
from invoice.common import table_util


class UserDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, id=None):
        super(UserDialog, self).__init__(parent)
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
            name = table_util.get_edit_text(self.name_lineEdit)
            login_name = table_util.get_edit_text(self.login_name_lineEdit)
            password = table_util.get_edit_text(self.password_lineEdit)
            password_again = table_util.get_edit_text(self.password_again_lineEdit)
            if self.is_admin_checkBox.isChecked():
                is_admin = 1
            else:
                is_admin = 0

            # 判断密码是否正确
            if password != password_again:
                QMessageBox.information(self.parentWidget(), "Information", u'两次输入的密码不一致！')
                return

            if self.id:
                # 修改
                q = User.update(name=name,
                                login_name=login_name,
                                password=password,
                                is_admin=is_admin).where(User.id == self.id)
                q.execute()
            else:
                # 添加
                user = User.create(name=name,
                                   login_name=login_name,
                                   password=password,
                                   is_admin=is_admin)
                user.save()

                # 刷新父窗体
                self.parent.user_query_btn_clicked()
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.exception(u"保存用户信息出错！")
            logger.error(e)

    def init_data(self, id):
        """
        根据用户ID，将用户的信息初始化到Dialog中
        :param id:客户ID
        :return:
        """
        try:
            user = User.get(id=id)
            self.name_lineEdit.setText(common_util.to_string_trim(user.name))
            self.login_name_lineEdit.setText(common_util.to_string_trim(user.login_name))
            self.is_admin_checkBox.setChecked(user.is_admin == 1)
        except NoSection.DoesNotExist:
            logger = logging.getLogger(__name__)
            logger.exception(u"程序出现异常")
