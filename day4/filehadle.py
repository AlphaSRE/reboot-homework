#import re
#read
f = open('file.txt')
for i in f.readlines():
    print i
f.close()
#strip space
f = open('file.txt')
l1 = []
l2 = f.readlines()
for i in l2:
    l1.append(i.strip('\n'))
f.close()
l4 = []
for i in l1:
    l3 = i.split(' ')
    for k,v in enumerate(l3):
        if v=='reboot':
           l3[k]='hello'
    l4.append(' '.join(l3))
f = open('file.txt','w')
f.writelines(l4)
f.close()
#change row2 wd
l2[1] = 'wd\n'
f = open('file2.txt','w')
f.writelines(l2)
f.write('i am good\n')
f.close()
