def add_all(*params):
    return reduce(lambda x,y: x+y,params)

def add_all2(*params):
    sum = 0
    for i in params:
        sum += i
    return sum

def add_all3(*params):
    return sum(params)

print add_all3(1,2,3,4,5)
