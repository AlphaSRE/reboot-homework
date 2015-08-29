def f1(n):
    i = 1
    for j in range(1,n+1):
        i *= j
    return i

print f1(5)

def f2(n):
    if n > 1:
        return n*f2(n-1)
    else:
        return 1

print f2(5)

def f3(n):
    return reduce(lambda x,y: x*y,range(1,n+1))

print f3(5)
