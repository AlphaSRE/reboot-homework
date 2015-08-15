#-*- coding: utf-8 -*-
#实现首字母大写的功能

str1 = raw_input('please input a string: ')

str1 = str1[0].upper() + str1[1:].lower()
print str1
