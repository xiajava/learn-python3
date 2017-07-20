#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def find(dir_path, key, root):
    if not os.path.isdir(dir_path):
        print('The input directory does not exist.')
        return
    for x in os.listdir(dir_path):
        abs_path = os.path.join(dir_path, x)
        if os.path.isfile(abs_path) and key in os.path.splitext(x)[0]:
            print('..%s' % abs_path[int(len(root)):])
        if os.path.isdir(abs_path):
            find(abs_path, key, root)


def findr(dir_path, key):
    root = dir_path
    find(dir_path, key, root)


d = input('the directory path: ')
k = input('the filename keyword: ')
findr(d, k)
