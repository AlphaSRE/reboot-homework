#coding: utf-8
import re
input_operation = raw_input('input a operation: ')

numsre = re.compile(r'[0-9]+')   #增加处理多位数
opsre = re.compile(r'[^0-9]+')

nums = numsre.findall(input_operation)
ops = opsre.findall(input_operation)

inputList = []
for i in range(len(nums)-1):
    inputList.append(nums[i])
    inputList.append(ops[i])
inputList.append(nums[-1])

def mycal(inputList):
    calList = []
    for k,v in enumerate(inputList): #优先处理*和/，得到只有+-的list
        if v == '*':
            val = float(calList.pop()) * float(inputList[k+1])
            calList.append(val) 
        elif v == '/':
            val = float(calList.pop())/float(inputList[k+1])
            calList.append(val)
        elif v == '+' or v == '-':
            calList.append(v)
        else:
            if k == 0:
                calList.append(v)
            elif type(calList[-1]) == float:
                pass
            else:
                calList.append(v)
    output = []
    for k,v in enumerate(calList):
        if v == '+':
            val = float(output.pop()) + float(calList[k+1])
            output.append(val)
        elif v == '-':
            val = float(output.pop()) - float(calList[k+1])
            output.append(val)
        else:
            if k == 0:
                output.append(v)
            
    print output[0]
            
mycal(inputList)
