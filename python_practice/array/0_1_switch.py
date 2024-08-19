arr = [1,0,1,0,1]
for i in range(len(arr)):
    if arr[i] == 0:
        arr[i] = 1
    else:
        arr[i] = 0
print(arr)