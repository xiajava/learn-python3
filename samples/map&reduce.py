#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1 规范名字
def normalize(name):
    return name[0].upper() + name[1:].lower()
    # return name.capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 2 求积
from functools import reduce
def prod(L):
    def mult(x, y):
        return x * y

    return reduce(mult, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 3 字符串转换成浮点数
from functools import reduce
def str2float(s):
    dot = 0
    sign = 1
    if s[0] == '-':  # 如果s有负号
        s = s[1:]  # 记下负号后所有字符，s的长度减1
        sign = -1  # # 负号记为-1
    for i in range(len(s)):
        if s[i] == '.':  # 如果s的第i位是小数点
            s = s[:i] + s[i + 1:]  # 删去小数点字符，s的长度减1
            dot = len(s) - i  # 记录小数点位数，小数点唯一
            break  # 运行一次后就跳出循环，因为s的长度本身发生变化

    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s)) / (10 ** dot) * sign


x1 = '123456789'
x2 = '123456.789'
x3 = '-123.456789'
print('str2float(\'', x1, '\') =', str2float(x1))  # str2float(' 123456789 ') = 123456789.0
print('str2float(\'', x2, '\') =', str2float(x2))  # str2float(' 123456.789 ') = 123456.789
print('str2float(\'', x3, '\') =', str2float(x3))  # str2float(' -123.456789 ') = -123.456789
