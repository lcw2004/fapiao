# -*- coding: utf-8 -*-
import logging

from PyQt4.QtGui import QDialog

from menu_config_ui import *


class MenuConfigDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, custom_id=None):
        super(MenuConfigDialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        # 绑定事件
        self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accepted)


    def accepted(self):
        """
        确定按钮事件
        :return:
        """
        try:
            pass
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
            pass
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.exception(u"程序出现异常")


    def setColor(self):
        newColor = QtGui.QColorDialog.getColor(self.paintColor)

        if newColor.isValid():
            self.paintColor = newColor
            palette = QtGui.QPalette(self.colorButton.palette())
            palette.setColor(QtGui.QPalette.Button, self.paintColor)
            self.colorButton.setPalette(palette)
            self.createImage()
            self.imageChanged.emit()
