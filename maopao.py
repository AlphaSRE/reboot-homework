arr = [9,8,7,6,5,4,3,2,1]
len_arr = len(arr)
for j in range(len_arr-1):
    for i in range(len_arr-j-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    print arr
