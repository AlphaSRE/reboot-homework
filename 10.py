while True:
    year = raw_input('input year: ')
    year = int(year) 
    if year%100==0:
        if year%400==0:
            print '%d is runnian' % year
            break
        else:
            print 'print %d is not runnian' % year
    else:
        if year%4==0:
            print '%d is runnian' % year
            break 
        else:
            print 'print %d is not runnian' % year
