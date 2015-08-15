#-*- coding: utf-8 -*-
#实现fromkeys的功能

def fromKeys(key,val=None):
    dic = {}
    for i in key:
        dic[i] = val
    return dic
d1 = fromKeys(['name','age'])
d2 = fromKeys(['name','age'],'wd')
print d1
print d2

