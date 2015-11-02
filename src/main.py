# -*- coding: utf-8 -*-

import sys
import logging
from PyQt4 import QtGui
from invoice.common import config


def init():
    # 设置项目编码
    import sys
    reload(sys)
    sys.setdefaultencoding('GBK')

    # 加载日志配置文件
    from invoice.log import logging_set
    logging_set.setup_logging()

    # 打印配置信息
    logger = logging.getLogger(__name__)
    logger.info(u"数据库文件:{0}".format(config.DATABASE_PATH))
    logger.info(u"模板XML文件:{0}".format(config.XML_PATH))


if __name__ == "__main__":
    init()

    app = QtGui.QApplication(sys.argv)
    from invoice.gui.mainwindow import MainWindow
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
