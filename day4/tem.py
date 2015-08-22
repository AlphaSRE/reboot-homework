f = open('tem.txt')
l1 = f.readlines()
f.close()
d = {}
for i in l1[1:]:
    l2 = i.split(' ')
    d[l2[0]]=l2[3].strip('\n')
l3 = []
for v in d.values():
    l3.append(v)

print 'the top: %s' % max(l3)
c = 0
for i in l3:
    c = c + float(i)
avg = c/len(l3)
print 'the avg: %f' % avg
