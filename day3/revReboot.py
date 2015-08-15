#-*- coding: utf-8 -*-
#反转reboot，不使用切片

str1 = 'reboot'
l1 = list(str1)
#l1.reverse()

l2 = []
#for i in l1:
#    l2.insert(0,i)
for i in range(len(l1)):
    l2.append(l1.pop())
str1 = ''.join(l2)
print str1
