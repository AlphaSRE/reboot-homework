def operate0(num1=0,num2=1,op=''):
    sum = 0
    if op == '+':
         sum = num1 + num2
    elif op == '-':
         sum = num1 - num2
    elif op == '*':
         sum = num1 * num2
    elif op == '/' and num2 != 0:
         sum = float(num1 / num2)
    else:
         print 'Error !!!!!!!!!!'
    return sum

def operate1(str1):
    str1 = '+' + str1
    arr1 = ['+','-']
    arr2 = ['*','/']
    arr3 = [1,'*']
    j = 0
    i = 1
    while i < len(str1):
        tmp1 = arr3[-1]
        tmp2 = arr3[-2]
        if i != len(str1) - 1:
            if str1[i] in arr1:
                num = float(str1[j+1:i].strip())
                arr3[-2] = float(operate0(tmp2,num,tmp1))
                arr3[-1] = str1[i]
                j = i
            elif str1[i] in arr2:
                num = float(str1[j+1:i].strip())
                if tmp1 in arr1:
                    arr3.append(num)
                    arr3.append(str1[i])
                elif tmp1 in arr2:
                    arr3[-2] = float(operate0(tmp2,num,tmp1))
                    arr3[-1] = str1[i]
                j = i
        else: 
            del arr3[-1]
            arr3[-1] = float(operate0(tmp2,float(str1[j+1:].strip()),tmp1))
        i = i + 1
    if len(arr3) == 1:
         print arr3[0]
    else:
        n = 1
        sum  = arr3[0]
        while n <  len(arr3):
            sum  = float(operate0(sum,arr3[n+1],arr3[n]))
            n = 2 * n + 1
        print arr3
        print sum

str1 = raw_input('please input:')
#str1 = '1*2'
operate1(str1)

