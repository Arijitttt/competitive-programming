def value_equal_to_index(arr,n):
    temp = []
    for  i in  range(n):
        #print(i)
        if i+1 == arr[i]:
            temp.append(arr[i])
    if temp:
        return temp
    else:
        return -1

arr = [15, 2, 45, 4 , 7]
print(value_equal_to_index(arr,n=len(arr)))
