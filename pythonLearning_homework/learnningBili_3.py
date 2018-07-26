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

# 函数使用的一些注意点：

#global 变量可以在函数定义中被访问，但是修改global variable的值时，python会在函数内部
# 定义一个和全局变量同名的局部变量，因此改变他的值只会修改局部同名变量的值而不会改变全局变量的值.
count = 5#全局变量
def myCount():
    count = 10#和global variable 同名的局部变量
    print('myCount() is called...:',count)

myCount();
print('========================================')
print(count)


print('===========***************************************========')
def myCount():
    global count#在声明全局变量后，可以直接改变他的值
    print("I am visiting global variable in myCount(),count = ",count)
    count = 10#和global variable 同名的局部变量
    print('myCount() is called...:',count)

myCount();
print('========================================')
print(count)

# 函数的内嵌，闭包
#函数的内嵌
"""
link:https://www.bilibili.com/video/av4050443/?p=21
"""
def fun1():
    print('fun1() is calling...')
    def fun2():
        print('fun2() is calling...')
    fun2()

fun1()
"""编译结果：
         fun1() is calling...
         fun2() is calling...
"""

# fun2()
'''编译结果：
         NameError: name 'fun2' is not defined
'''
# 因为fun2()是在fun1()内部定义的，作用域只在fun1()内部，外部对他是不可见的
# 如果fun1不调用他，那么谁也不能调用它

#========================================================================
#函数的闭包
def myfun1(x):
    def myfun2(y):
        return x*y
    return myfun2#python的返回值可以是任何类型

a = myfun1(5)
print(a)
i = type(a)
print(i)
# -----<class 'function'>
i = a(8)
print(i)

b = myfun1(8)(10)
print(b)

######################################################################
######################lambda表达式#####################################
#=====================================================================
'''
link:https://www.bilibili.com/video/av4050443/?p=22
'''
def add(x1,y1):
    return x1+y1
add(4,4)
#使用lambda定义表达式可以精简函数定义，和函数命名，其功能和函数一样
g = lambda x,y : x+y
g(4,4)
#=======================================================================
