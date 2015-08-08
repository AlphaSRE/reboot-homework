import sys
count=0
sum=0
while True:
    getNumber=''
    getNumber = raw_input('input a number : ')
    if getNumber=='':
        break
#    else if type(getNumber)==str:
#        print 'get a str,please input a number '
#        continue
        
    count += getNumber
    sum += 1
if sum==0:
    
    sys.exit()
avg = float(count)/float(sum)
print 'the averge is : {0}'.format(avg)
