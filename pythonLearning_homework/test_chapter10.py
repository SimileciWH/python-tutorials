#!usr/bin/env python3
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
# # 10-1test
filePath = r'/home/simileciwh/Documents/python_work/pythonLearning_homework/test10-1.txt'
with open(filePath) as p:
    contents = p.read()
    print(contents)


# 10-2test
# filePath = r'/home/simileciwh/Documents/python_work/pythonLearning_homework/test10-1.txt'
# with open(filePath) as p1:
#     lines = p1.readlines()
# contents1 = ''
# for line in lines:
#     contents1 += line.rstrip()
# print(contents1.replace('python','c'))
# print(contents1)
#
# # 10-3,10-4,10-5test
# fileName = 'research.txt'
#
# print('Why u like to write comprome? Answer it with writing your name and reason.')
# print('Press \'q\'to stop!')
# with open(fileName,'r+') as p:
#     while True:
#         name = input('Please input your name:\n\t\t')
#         if name == 'q':
#             break
#         reason = input('Reason:\n\t\t')
#         if reason == 'q':
#             break
#         p.write('\n'+name+', reason: '+reason+'\n')
#     print('===========================================================')
#     print('Display contents in research.txt as following:\n')
#     contents_in = p.read()
#     print(contents_in)
#
# # 10-6test
# print('Please enter \'q\' to end this programe!')
# while True:
#     num = input('input numbers:\n')
#     if num == 'q':
#         break
#     try:
#         num = int(num)
#     except :
#         print("Please input numbers not woeds!!!")
#     else:
#         print(num)
