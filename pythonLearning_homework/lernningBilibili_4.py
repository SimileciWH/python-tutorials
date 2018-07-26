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
#==============================================字典的学习===============================
# 使用dict()function 创建字典
dictionary1 = dict((('1','one'),('2','two'),('3','three')))
dictionary1['1']

dictionary2 = dict(((1,'one'),(2,'two'),('3','three')))
dictionary2[1]

dictionary2['4'] = 'four'#当字典中不存在一个键值对时，字典会自动创建

#===========================================集合=======================================
num = {2,1,4,5,6,8}

num2 = {2,1,4,5,6,8,8,6,5,4,1,2}
#集合中的元素是唯一的，有序的，重复的元素会被删除，元素按照默认规则排序，不一定是从小到大
#=============================================
#==================set()创建集合===============
#=============================================
set1 = set([6,1,2,3,4,5])

set2 = frozenset([1,2,3,4,5])#不可改变的集合，相当于元祖

#===========文件操作============
filepath = r'/home/simileciwh/Documents/python_work/pythonLearning_homework/test10-1.txt'
with open(filepath,'r') as p:
    print(p.read())

with open(filepath,'a') as p:
    p.writelines('2018-07-26 15:54')
    p.write('This is fisrt time in ubuntu 18.04 LTS write code!!!')
    p.write('\tThis is fisrt time in ubuntu 18.04 LTS write code!!!')