def array_leaders(arr):
    temp = []
    base = arr[-1]
    temp.append(base)
    print(temp)
    for i in range(len(arr)-2,-1,-1):
        if arr[i] >= base:
            base = arr[i]
            temp.append(arr[i])
    return temp[::-1]

arr = [16, 17, 4, 3, 5, 2]
print(array_leaders(arr))