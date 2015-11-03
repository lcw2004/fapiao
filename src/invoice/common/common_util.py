# -*- coding: UTF-8 -*-

import re

def to_string_trim(input_str):
    """
    将其他类型转为字符串
    """
    if input_str is None:
        input_str = ""
    return input_str

def float_to_string(input_str):
    u"""
    如果是浮点型，转为int类型再转字符串
    """
    output_str = input_str
    if type(input_str) == float:
        output_int = int(input_str)
        output_str = str(output_int)
    return output_str

def is_blank_str(input_str):
    """
    判断是否是空字符串
    """
    if input_str and len(input_str) > 0:
        return False
    else:
        return True

def has_chinese_charactar(input_str):
    """
        判断字符串是否有中文
        :param input_str:需要判断的字符串
        :return:True-包含; False-不包含
    """
    input_unicode_str = unicode(input_str)
    zh_patten = re.compile(u'[\u4e00-\u9fa5]+')
    match = zh_patten.search(input_unicode_str)
    res = False
    if match:
        res = True
    return res

def save_to_file(content, path):
    """
    将文件保存到指定路径
    :param content:文件内容
    :param path:文件路径
    """
    f = open(path, 'w')
    f.write(content)
    f.close()

def read_from_file(path):
    """
    从文件里面读取信息
    :param path:文件路径
    """
    f = open(path, 'r')
    return f.read()

def is_file_exists(path):
    """
    判断文件是否存在
    :param path:文件路径
    """
    import os.path
    return os.path.exists(path)