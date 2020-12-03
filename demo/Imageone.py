#!/usr/bin/python
# coding=utf-8

# 图片转TXT 非命令行模式

from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('/tools/timg.jpeg')
k,j = im.size
print k
print j
im = im.resize((80,40),Image.NEAREST)
txt = '  '
for i in range(40):
    for j in range(80):
        txt += get_char(*im.getpixel((j,i)))
    txt += '\n'
print txt

f = open("/tools/my2.txt", "w")
f.write(txt)



