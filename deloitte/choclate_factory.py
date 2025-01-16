def chcolate_factory(arr,n):
    temp = []
    for i in range(n-1,-1,-1):
        if arr[i] == 0:
            temp.append(arr[i])
            arr.remove(arr[i])
    arr = arr+temp
    return arr
arr = [4,5,0,1,9,0,5,0]
n = len(arr)
print(chcolate_factory(arr,n))