dic1 = {'name':'subin','age':20,'c':[1,2]}

def cp(dic):
    newDic = {}
    for k in dic:
        newDic[k] = dic[k]
    return newDic

dic2 = cp(dic1)

dic2['c'][0] = 3
print dic1
print dic2
