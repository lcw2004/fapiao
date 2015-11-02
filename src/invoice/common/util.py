# -*- coding: UTF-8 -*-

import os


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
