L = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

a = 0
s = 0
for idx,v in enumerate(L):
    if a < v:
        a = v
        s = idx
print s,a
