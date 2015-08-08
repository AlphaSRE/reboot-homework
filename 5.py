#!/usr/bin/env python
#
inputNumber=''
count=0
while True:
    inputNumber = raw_input('input a number : ')
    if inputNumber == 'pc':
        break
    else:
        count = count+int(inputNumber)

print 'The count is : %s' % count
