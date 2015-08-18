def add_all(*params):
    return reduce(lambda x,y: x+y,params)

print add_all(1,2,3,4,5)
