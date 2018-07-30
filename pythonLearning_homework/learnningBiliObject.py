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
'''
OO----object oritention     ，op----object programme
                OO面向对象的特征
封装----讲函数，或者类包含起来，别人无法知道
继承----子类继承拥有父类的所有属性和方法
多态----不同对象对同一方法响应不同的行动
'''

#多态例子

#A,B是不同的类
class A(object):
    def fun(self):
        print('我是A类...')

class B(object):
    def fun(self):
        print('我是B类...')

#不同的类生成不同的实例
a = A()
b = B()

#调用同一种方法
a.fun()
b.fun()

'''
响应不同的行为：（运行结果：）
                        -----我是A类...
                        -----我是B类...
'''
########################################################
#在python中定义私有变量只需要在变量名或函数名前加上“__”,两个下划线就变成伪私有的了
########################################################
class C(object):
    def __init__(self,name):
        self.name = name
    def view(self):
        print('who is calling C ?:%s' % self.name)
c = C('darling')
c.name
c.view()
'''
输出结果:
        'darling'
        who is calling C ?:darling
'''

class D(object):
    def __init__(self,name):
        self.__name = name#在name前加上两个'__',使其变成伪私有变量，外部无法访问
    def view(self):
        print('who is calling D ?:%s' % self.__name)

'''
运行结果：
            >>>d = D('sdas')
            >>>d.view()
                    who is calling D ?:sdas
            >>>d.name
                    Traceback (most recent call last):
                      File "<input>", line 1, in <module>
                    AttributeError: D instance has no attribute 'name'
            >>>d.__name
                    Traceback (most recent call last):
                      File "<input>", line 1, in <module>
                    AttributeError: D instance has no attribute '__name'
'''
'''
但是python的私有化机制，其实只是讲__name重命名成_类名__成员名,运行结果如下所示：
            >>>d._D__name
                    'sdas'
'''

#=========================================================================================
#===================================继承===================================================
#=========================================================================================

class Restaurant(object):
    def __init__(self,restaurant_name,restaurant_type):
        '''随便创建一个餐厅的信息'''
        self.name = restaurant_name
        self.type = restaurant_type
        self.number_served = 0

    def describle_restaurant(self):
        print('This restaurant is called '+self.name.title()+', and it\'s a '+self.type.title()+' kind restaurant.')

    def open_restaurant(self):
        print('The restaurant is now openning all day!')

    def set_number_served(self,number_served):
        prompt = 'There have '+str(number_served)+' people eated!'
        print(prompt)

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,restaurant_type,flavors):


        super(IceCreamStand,self).__init__(restaurant_name,restaurant_type)
        #python2和python3在super()使用时有差别，2需要参数，3不需要


        self.flavors = flavors

    def display_icecream(self):
        # 子类无法访问父类的参数，失败的尝试如下：
        # prompt = 'The'+self.restaurant_name.title()+' restaurant is a '+self.restaurant_type.title()
        # prompt += ' kind of restaurant.\n'+'The ice-cream with following adds:\n\t'
        # print(prompt)
        print('The ice-cream with following adds:\n\t')
        for flavor in self.flavors:
            print(flavor)
'''
调试结果：
            >>>generalR = Restaurant('jinlin','chinese')
            >>>iceR = IceCreamStand('OCOC','forigen',['12','21','233'])
            >>>generalR.describle_restaurant()
                    This restaurant is called Jinlin, and it's a Chinese kind restaurant.
            >>>generalR.set_number_served(4)
                    There have 4 people eated!
            >>>generalR.open_restaurant()
                    The restaurant is now openning all day!
            >>>iceR.describle_restaurant()
                    This restaurant is called Ococ, and it's a Forigen kind restaurant.
            >>>iceR.set_number_served(9)
                    There have 9 people eated!
            >>>iceR.open_restaurant()
                    The restaurant is now openning all day!
            >>>iceR.display_icecream()
                    The ice-cream with following adds:
                        
                    12
                    21
                    233
'''

#PS:
"""
将不同的类结合到一起；
        如果是横向关系，那么就用组合----没有风险
        如果是纵向关系，那么就用继承----重复继承有风险高，出BUG
"""

class Turtle(object):
    def __init__(self,x):
        self.num = x

class Fish(object):
    def __init__(self,x):
        self.num = x
class Pool(object):
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    def display(self):
        print('There are %d turtles and %d fishes in pool' % (self.turtle.num,self.fish.num))

pool = Pool(2,23)
pool.display()
"""
调试结果：
        There are 2 turtles and 23 fishes in pool
"""




'''
与类相关的BIF
link:https://www.bilibili.com/video/av4050443/?p=41
python可以通过 import sys   link:https://www.bilibili.com/video/av4050443/?p=52
               sys.path查看python系统的模块，可以通过
               sys.path.append()将新的位置加入到系统搜索路径中
               
python，当项目中模块过多时，可以通过打包将模块放到包中管理；
新建文件夹，将需要放到一起的模块直接拷贝到该文件夹下
注意！！！该文件夹下一定要包含一个__init__.py的文件，可以使空文件
__init__.py是告诉python这是一个包文件

调用包中的模块：
import <pkg>.module as <...>
from <pkg>.module import *

'''
