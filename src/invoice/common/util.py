# -*- coding: UTF-8 -*-

from PyQt4 import QtGui

from invoice.dao.DictDao import DictDao
from invoice.common import excelparse
import os
from invoice.common import tableUtil



# 将文件保存到指定路径
def saveAsTemp(content, path):
    f = open(path, 'w')
    f.write(content)
    f.close()

# 从文件里面读取信息
def readFromFile(path):
    f = open(path, 'r')
    return f.read()

# 判断文件是否存在
def isFileExists(path):
    return os.path.exists(path)
