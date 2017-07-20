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


# 验证并提取出带名字的Email地址 <Tom Paris> tom@voyager.org
def is_email2(txt):
    s_space = re.split(' ', txt)
    is_email(s_space[-1])

    s_name = re.split(s_space[-1], txt)
    print('name:', s_name[0])


add4 = '<Tom Paris> tom@voyager.org'
is_email2(add4)

'''
------------------------
email add: someone@gmail.com
s_at: ['someone', 'gmail.com']
s_dot: ['someone@gmail', 'com']
username ok
ok
------------------------
email add: bill.gates@microsoft.com
s_at: ['bill.gates', 'microsoft.com']
s_dot: ['bill', 'gates@microsoft', 'com']
username ok
ok
------------------------
email add: tom@voyager.org
s_at: ['tom', 'voyager.org']
s_dot: ['tom@voyager', 'org']
username ok
ok
name: <Tom Paris> 
'''
