#-*- coding: utf-8 -*-
#实现用户输入员工名字与id

users = raw_input('please input username and id: ')

splitUsers = users.split(',')
dic = {}
for i in range(len(splitUsers)):
    lst = splitUsers[i].split(':')
    dic[lst[0]] = lst[1]

print dic.items()
