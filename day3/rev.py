#-*- coding: utf-8 -*-
#把一个dict的key和value反转
#两次反转返回最初字典

def rev(dic):
    newDic = {}
    for key,val in dic.items():
        if val not in newDic:
            newDic[val] = key
        else:
            if isinstance(newDic[val],list):
                newDic[val].append(key)
            else:
                newDic[val] = [newDic[val],key]
    return newDic
def rev2(dic):
    newDic = {}
    for key,val in dic.items():
        if isinstance(val,list):
            for i in val:
                newDic[i] = key
        else:
            newDic[val] = key
    return newDic

d = {'teach':'pc','waihao':'pc','name':'pc','age':12,'job':'IT'}
print rev(d)
print rev2(rev(d))
