#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

'''
用户名@域名
用户名：只包含大小写字母，数字，点(.)，连字符(-)和下划线(_),开头和结尾不能是点，并且点不能连在一起
域名:只包含大小写字母，数字，点(.)和连字符(-)，开头和结尾不能是点，并且点不能连续
'''


def is_email(add):
    print('------------------------')
    print('email add:', add)
    # 判断@
    s_at = re.split('@', add)
    print('s_at:', s_at)
    if len(s_at) != 2:
        print('failed: @ error')
        return False
    # 判断点
    s_dot = re.split('\.', add)
    print('s_dot:', s_dot)
    if '' in s_dot:
        print('failed: dots error')
        return False
    # 判断用户名
    if re.match('(^\w[0-9a-zA-Z\-\.\_]*\w$)|(^\w$)', s_at[0]):
        print('username ok')
    else:
        print('failed: username')
        return False
    # 判断域名
    if re.match('(^\w[0-9a-zA-Z\-\.]*\w$)|(^\w$)', s_at[1]):
        print('ok')
        return True
    else:
        print('failed: domain name')
        return False


add1 = 'someone@gmail.com'
add2 = 'bill.gates@microsoft.com'
is_email(add1)
is_email(add2)
