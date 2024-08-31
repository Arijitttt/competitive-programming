def largestElement(arr, n):
    m = arr[0]
    for i in range(1,n):
        if arr[i]>m:
            m = arr[i]
    return m
print(largestElement(arr=[1,2,3,4,5],n=5))