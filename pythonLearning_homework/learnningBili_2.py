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
list = [123,456,['nancy','david'],102]
print(list)
print('\n')

a = 123 in list
print('123 in list ?')
print(a)
print('\n')

b = 'nancy' in list
print("'nancy' in list?")
print(b)
print('\n')

c = 'nancy' not in list
print("'nancy' not in list?")
print(c)
print('\n')

d = 'nancy' in list[2]
print("'nancy' in list[2]?")
print(d)
print('\n')

list2 = list*10
print('list2 = list*10')
print('list2:')
print(list2)
print('\n')

print('====================================================================')
print('显示所有关于列表的方法:')
print(dir(list))

a = list2.count(123)
print '"123"在list2中出现了多少次？'
print(a)

list3 = list[:]
print(list3)

# ==========================================关！！！于元祖的笔记！！！=====================================
"""
python 中元祖的标志不是()（小括号）而是(,)（小括号加逗号）！！！
example：
a = (1)
type(a)
-----<class 'int'>
a = (1,)
type(a)
-----<class 'tuple'>
a = 1,
type(a)
-----<class 'tuple'>
link:https://www.bilibili.com/video/av4050443/?p=14
元祖是可以被重组，del，in,not in...的
"""

# ======================================================================================================
# ===========================================格式控制字符===========================================
print('========================================================================')
print('%s' % 'hello world!!!')
# '%s' % 'msgs'中的第二个 % 是将'msgs'替换到 %s 中去的
print('%d+%d=%d' % (4,5,4+5))

print('%.2f' % 3.141592)
print('%6.2f' % 3.141592)   #6个字符，小数位2个，整数位3个，小数点也占一位
print('%+.5f' % 3.141592)   #显示加号
