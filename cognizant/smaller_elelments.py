def check(arr,n,ind):
    i = ind-1
    j = ind+1

    while i >= 0:
        if arr[i]>arr[ind]:
            return False
        i -= 1
    
    while j< n:
        if arr[j]<arr[ind]:
            return False
        j += 1
    return True

def findElement(arr,n):
    for i in range(1,n-1):
        if check(arr,n,i):
            return i
    return -1
arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
n = len(arr)
print(findElement(arr,n))