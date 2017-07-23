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
        # size, move, Header = info[2], info[4], info[5]
        ptype, Reserved_bit, width, height, one, colors = info[0:2], info[3], info[6], info[7], info[8], info[9]
        print('bmp_info:', info)
        if Reserved_bit == 0 and one == 1 and (ptype == (b'B', b'M') or ptype == (b'B', b'A')):
            if ptype == (b'B', b'M'):
                print('Type: Windows bitmap')
            else:
                print('Type: OS/2 bitmap')
            print('Image Size: %s*%s' % (width, height))
            print('Colors:', colors)
    except:
        print('not bitmap')
        return


d = input('the file path: ')
is_bmp(d)
