arr = [4,5,0,1,9,0,5,0]
n = len(arr)
for i in range(n-1,-1,-1):
    if arr[i] == 0:
        arr.remove(arr[i])
        arr.append(0)
print(arr)
