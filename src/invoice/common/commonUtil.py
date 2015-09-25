# -*- coding: UTF-8 -*-

import re

# 将其他类型转为字符串

def to_string_trim(uString):
    return uString

# 如果是浮点型，转为int类型再转字符串
def float_to_string(uString):
    output = uString
    if type(uString) == float:
        outputInt = int(uString)
        output = str(outputInt)
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

if __name__ == "__main__":
    s = "  \t a string example\t  "
    s = s.strip()
    print to_string_trim(s)