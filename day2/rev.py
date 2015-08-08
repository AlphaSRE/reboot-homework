a = [1,2,8,5,4]
print a
for i in range(len(a)-1):
    a[i:i] = [a.pop()]
print a
