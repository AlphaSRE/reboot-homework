l = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
l2 = []
for i in l:
    if i not in l2:
        l2.append(i)
print l2
