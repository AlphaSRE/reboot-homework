import random
arr1 = [9,8,7,6,5,4,3,2,1]
random.shuffle(arr1)
print arr1
arr2 = []

for k,v in enumerate(arr1):
    if k == 0:
        arr2.append(v)
    else:
        for i in range(len(arr2)):
            if v > arr2[len(arr2)-i-1]:
                arr2.insert(len(arr2)-i,v)
                break
        else:
            arr2.insert(0,v)

print arr2
