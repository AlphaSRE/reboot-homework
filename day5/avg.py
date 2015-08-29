def avg(*params):
    sum = 0
    for i in params:
        sum += i
    return float(sum)/len(params)
print avg(0)
