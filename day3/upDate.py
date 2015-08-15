#-*- coding: utf-8 -*-
#实现字典的update功能

dic1 = {'name':'wd'}
dic2 = {'name':'subin','age':'12'}
for key in dic2:
    dic1[key] = dic2[key]

print dic1
