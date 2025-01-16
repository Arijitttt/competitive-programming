def choclate(arr,n):
    temp = []
    for i in range(n-1,-1,-1):
        if arr[i] == 0:
            temp.append(arr[i])
            arr.remove(arr[i])
    arr = arr+temp
    return arr
arr = list(map(int,input().split()))
print(choclate(arr,len(arr)))