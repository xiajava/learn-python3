#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random


# 随机字母:
def rndChar():
    # 随机数字
    numChr = str(random.randint(0, 9))
    # 随机字母
    uChr = chr(random.randint(65, 90))
    lChr = chr(random.randint(97, 122))
    return random.choice((numChr, uChr, lChr))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象: win环境ImageFont()内字体arial.ttf小写
font = ImageFont.truetype('arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
code = ''
for t in range(4):
    rndc = rndChar()
    draw.text((60 * t + 10, 10), rndc, font=font, fill=rndColor2())
    code += rndc
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('%s.jpg' % code, 'jpeg')
