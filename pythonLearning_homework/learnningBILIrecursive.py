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

#迭代实现阶乘计算
def factorial(n):
    a = n
    for i in range(1,n):
        a *= i
    return a
factorial(5)

#递归实现阶乘计算
def factorial2(n):
    if n == 1:#递归的结束条件
        return 1
    else:#调用自生的条件
        a = n*factorial(n-1)#调用自生的语句
        return a
'''总结：！！！只有天才的程序员，才会使用递归！！！
递归算法的使用条件：
1、有结束条件，（最先写）
2、有符合递归的条件
3、函数调用自生
'''

#使用迭代实现斐波那契额数列
def feibo(month):
    listnum = []
    fn = 1
    fn1 = fn2 = 0
    for i in range(1,month+1):
        if i == 1 or i == 2:
            fn = fn1 = fn2 = 1
            listnum.append(fn)
        else:
            fn = fn1+fn2
            fn2 = fn1
            fn1 = fn
            listnum.append(fn)
    return listnum

#使用递归实现斐波那契额数列
def feibo2(month):
    fn = 1
    if month == 1 or month == 2:
        return 1
    else:
        fn = feibo2(month-1)+feibo2(month-2)
        print(fn)#通过查看打印的数据，可以发现数据的重复计算
        return fn
