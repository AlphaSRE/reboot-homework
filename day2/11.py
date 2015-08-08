L = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js']
d = {}
for val in L:
    if val in d:
        d[val] += 1
    else:
        d[val] = 1

for k in d:
    print '%-6s:%s' % (k,d[k])
