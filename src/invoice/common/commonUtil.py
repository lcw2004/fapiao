# -*- coding: UTF-8 -*-

# 将其他类型转为字符串
import re

def to_string(uString):
    output = uString
    if type(uString) == float:
        output = str(uString)
    return output

# 判断是否是空字符串
def is_blank_str(s):
    if s and len(s) > 0:
        return False
    else:
        return True

# 判断字符串是否有中文
def has_chinese_charactar(content):
    iconvcontent = unicode(content)
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zhPattern.search(iconvcontent)
    res = False
    if match:
        res = True
    return res