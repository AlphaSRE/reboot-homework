#-*- coding: utf-8 -*-
#实现字典keys的功能

def Keys(dic):
    keys = []
    if isinstance(dic,dict):
        for key in dic:
            keys.append(key)
    else:
        print 'not a dict'
    return keys

d = {'name':'wd','age':'10'}
print Keys(d)
