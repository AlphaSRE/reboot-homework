f = open('hello.txt')
while True:
    a = f.read(1)
    if a:
        print a
    else:
        break
