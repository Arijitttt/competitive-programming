arr = [-3, -1, 0, 1, 2]

for i in range(len(arr)):
    arr[i] = arr[i]*arr[i]

arr = sorted(arr)
print(arr)