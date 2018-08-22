# !/usr/bin/env python
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
#
print( " hello world" )

a = "hello world"
print( a )
# def callback(data=123):
#     print('I got '+str(data)+' in math examination')
#
# def printff():
#     callback()
#
# if __name__=='__main__':
#     printff()
def sum_pingfang(numbers):
    sum = 0
    for number in numbers:
        sum += number*number
    return sum
a = sum_pingfang([1,2,3])
b = [1,2,3,4]
c = sum_pingfang(b)

print 'a = %d,b = %d' % (a,c)

# 使用可变参数
def sum_pingfang_1(*numbers):
    sum = 0
    for number in numbers:
        sum += number*number
    return sum
d = sum_pingfang_1(1,2,3,4)
e = [1,2,3,4]
f = sum_pingfang_1(*e)

print 'd = %d,f = %d' % (d,f)
