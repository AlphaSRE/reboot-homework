s = raw_input('adsaf')
s1 = []
for i in s.split(','):
    s1.append(tuple(i.split(':')))

print s1
