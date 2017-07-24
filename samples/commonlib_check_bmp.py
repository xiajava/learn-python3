#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
import struct


def is_bmp(p_path):
    try:
        with open(p_path, 'rb') as f:
            info = struct.unpack('<ccIIIIIIHH', f.read(30))
            print('file info:', info)
    except:
        print('open error')
        return

    # size, move, Header = info[2], info[4], info[5]
    p_type, Reserved_bit, width, height, one, colors = info[0:2], info[3], info[6], info[7], info[8], info[9]

    if Reserved_bit == 0 and one == 1 and (p_type == (b'B', b'M') or p_type == (b'B', b'A')):
        if p_type == (b'B', b'M'):
            print('Type: Windows bitmap')
        else:
            print('Type: OS/2 bitmap')

        print('Image Size: %s*%s' % (width, height))
        print('Colors:', colors)
        return
    else:
        print('not bitmap')
        return


path = input('file path: ')
is_bmp(path)
