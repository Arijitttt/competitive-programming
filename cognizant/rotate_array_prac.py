def rotate(arr,d):
    n = len(arr)
    for i in range(d):
        fisrt = arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]
        arr[n-1] = fisrt
    return arr
print(rotate([1,2,3],1))