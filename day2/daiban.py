thing = []
while True:
    order = raw_input('do some things: ')
    if order=='add':
        input = raw_input('please input something: ')
        thing.append(input)
        print thing
    if order=='do':
        if thing!=[]:
            print thing.pop()
        else:
            break
