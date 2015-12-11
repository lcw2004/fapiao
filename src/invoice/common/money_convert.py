# -*- coding: utf-8 -*-
import logging

import math


def to_rmb_upper(num):
    cap_unit = [u'万', u'亿', u'万', u'圆', '']
    cap_digit = {2: [u'角', u'分', ''], 4: [u'仟', u'佰', u'拾', '']}
    cap_num = [u'零', u'壹', u'贰', u'叁', u'肆', u'伍', u'陆', u'柒', u'捌', u'玖']
    last = u'整'
    s_num = str('%019.02f') % num
    if s_num.index('.') > 16:
        return ''
    ret, node_num, sub_ret, sub_chr = '', '', '', ''
    cur_chr = ['', '']
    for i in range(5):
        j = int(i * 4 + math.floor(i / 4))
        sub_ret = ''
        node_num = s_num[j:j + 4]
        lens = len(node_num)
        for k in range(lens):
            if int(node_num[k:]) == 0:
                continue
            cur_chr[k % 2] = cap_num[int(node_num[k:k + 1])]
            if node_num[k:k + 1] != '0':
                cur_chr[k % 2] += cap_digit[lens][k]
            if not ((cur_chr[0] == cur_chr[1]) and (cur_chr[0] == cap_num[0])):
                if not ((cur_chr[k % 2] == cap_num[0]) and (sub_ret == '') and (ret == '')):
                    sub_ret += cur_chr[k % 2]
        sub_chr = [sub_ret, sub_ret + cap_unit[i]][sub_ret != '']
        if not ((sub_chr == cap_num[0]) and (ret == '')):
            ret += sub_chr
    rmb_cn = [ret, cap_num[0] + cap_unit[3]][ret == ''] + last

    # logger = logging.getLogger(__name__)
    # logger.info(u"RMB:{0} -> {1}".format(num, rmb_cn))
    return rmb_cn
