l = [(1,4),(5,1),(2,3)]
l2 = sorted(l,key=lambda x:max(x))

l3 = sorted(l,key=lambda x : (x[0] > x[1]) * x[0] + (x[0] <= x[1]) * x[1])
print l
