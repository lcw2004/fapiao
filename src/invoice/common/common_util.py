# -*- coding: UTF-8 -*-

import re

def to_string_trim(input_str):
    """
    将其他类型转为字符串
    """
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
