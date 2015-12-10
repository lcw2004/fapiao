# -*- coding: utf-8 -*-

import logging
import sys

from PyQt4 import QtGui
from PyQt4.QtCore import QTranslator, QLocale

from invoice.common import config
from invoice.gui.login import LoginDialog
from invoice.gui.mainwindow import MainWindow


def init():
    # 设置项目编码
    import sys
    reload(sys)
    sys.setdefaultencoding('GBK')

    # 加载日志配置文件
    from invoice.log import logging_set
    logging_set.setup_logging(config.PATH_OF_LOGGING)

    # 打印配置信息
    logger = logging.getLogger(__name__)
    logger.info(u"数据库文件:{0}".format(config.PATH_OF_DATABASE))
    logger.info(u"模板XML文件:{0}".format(config.PATH_OF_XML))


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
