#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
import os
def find(dir_path, key):
    if not os.path.isdir(dir_path):
        print('The input directory does not exist.')
        return
    for x in os.listdir(dir_path):
        abs_path = os.path.join(dir_path, x)
        if os.path.isfile(abs_path) and key in os.path.splitext(x)[0]:
            print(abs_path)
        if os.path.isdir(abs_path):
            find(abs_path, key)


d = input('the directory path: ')
k = input('the filename keyword: ')
find(d, k)
