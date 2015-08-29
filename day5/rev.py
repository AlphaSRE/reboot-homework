#-*- coding: utf-8 -*-
#把一个dict的key和value反转
#两次反转返回最初字典
#函数为fuc（D1,D2，REV）

def rev(dic1,dic2 = {}, rev = False):
    newDic = {}
    for key,val in dic1.items():
        if val not in newDic:
            newDic[val] = key
        else:
            if isinstance(newDic[val],list):
                newDic[val].append(key)
            else:
                newDic[val] = [newDic[val],key]
    dic2 = newDic
    if rev == False:
        return dic2
    if rev == True:
        return rev2(dic2) #调用rev2函数进行二次反转
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
print rev(d,{'subin':'wd'})
print rev(d,rev=True)
#print rev2(rev(d))
