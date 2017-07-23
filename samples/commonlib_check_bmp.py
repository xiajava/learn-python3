#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
import struct
import os


def is_bmp(d):
    if not os.path.isfile(d):
        print('The file path does not exist.')
        return
    try:
        with open(d, 'rb') as f:
            info = struct.unpack('<ccIIIIIIHH', f.read(30))
        type = info[0:2]
        # size = info[2]
        Reserved_bit = info[3]
        # move = info[4]
        # Header = info[5]
        height = info[6]
        high = info[7]
        one = info[8]
        colors = info[9]
        print('bmp_info:', info)
        if Reserved_bit == 0 and one == 1 and (type == (b'B', b'M') or type == (b'B', b'A')):
            if type == (b'B', b'M'):
                print('Type: Windows bitmap')
            else:
                print('Type: OS/2 bitmap')
            print('Image Size: %s*%s' % (height, high))
            print('Colors:', colors)
    except:
        print('not bitmap')
        return


d = input('the file path: ')
is_bmp(d)
