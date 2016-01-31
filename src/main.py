# -*- coding: utf-8 -*-

import logging
import sys

from PyQt4 import QtGui
from PyQt4.QtCore import QTranslator

from invoice.common import config
from invoice.common.settings import Settings
from invoice.gui.login import LoginDialog
from invoice.gui.mainwindow import MainWindow
from invoice.log import logging_set


def init():
    # 设置项目编码
    import sys
    reload(sys)
    sys.setdefaultencoding('GBK')

    import os
    program_path = os.getcwd()
    config.PROGRAM_PATH = program_path

    # 加载日志配置文件
    logging_set.setup_logging(config.PATH_OF_LOGGING)

    # 打印配置信息
    logger = logging.getLogger(__name__)
    logger.info(u"数据库文件:{0}".format(config.PATH_OF_DATABASE))
    logger.info(u"模板XML文件:{0}".format(config.PATH_OF_XML))

    # 初始化默认配置
    Settings.set_value_if_null(Settings.TEMP_FONT_NAME, config.TEMP_FONT_NAME)
    Settings.set_value_if_null(Settings.TEMP_FONT_SIZE, config.TEMP_FONT_SIZE)
    Settings.set_value_if_null(Settings.INTERFACE_INPUT_PATH, config.INTERFACE_INPUT_PATH)
    Settings.set_value_if_null(Settings.INTERFACE_OUTPUT_PATH, config.INTERFACE_OUTPUT_PATH)
    Settings.set_value_if_null(Settings.INTERFACE_TEMP_PATH, config.INTERFACE_TEMP_PATH)
    Settings.set_value_if_null(Settings.INVOICE_START_NUM, "0")
    Settings.set_value_if_null(Settings.INVOICE_END_NUM, "0")
    Settings.set_value_if_null(Settings.INVOICE_CURRENT_NUM, "0")

if __name__ == "__main__":
    init()

    logger = logging.getLogger(__name__)
    try:
        app = QtGui.QApplication(sys.argv)

        # 加载I18N文件
        qtTranslator = QTranslator()
        if qtTranslator.load(config.PATH_OF_I18N_CH_CN):
            logger.info(u"加载QLocale文件：" + config.PATH_OF_I18N_CH_CN)
            app.installTranslator(qtTranslator)

        # 加载登录界面
        login_dialog = LoginDialog()
        login_dialog.show()
        if login_dialog.exec_():
            window = MainWindow()
            window.show()

        sys.exit(app.exec_())
    except Exception as e:
        logger.exception(u"程序出现异常")
        logger.error(e)
