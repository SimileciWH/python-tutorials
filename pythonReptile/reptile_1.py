#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '$Package_name'
__author__ = '$USER'
__mtime__ = '$DATE'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
#从placekitten网站下载图片
import urllib as ul
backWeb = ul.urlopen('http://placekitten.com/500/400')
# type(backWeb)-----<type 'instance'>
#              -----<addinfourl at 140534374010104 whose fp = <socket._fileobject object at 0x7fd0b573b1d0>>

cat_54_img = backWeb.read()

filepath = r'\home\simileciwh\Documents\python_work\pythonReptile\cat.jpg'

with open('cat.jpg','wb') as p:
    p.write(cat_54_img)
