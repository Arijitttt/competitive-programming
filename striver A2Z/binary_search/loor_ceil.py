def getFloorAndCeil(arr,x):
    arr.sort()
    low = 0
    high = len(arr)-1
    fl,cl =-1,-1
    res = []
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == x:
                fl = cl = arr[mid]
                break
        if arr[mid]<x:
            # res.append(arr[mid])
            fl = arr[mid]
            low = mid+1
            
        else:
            # res.append(arr[mid])
            cl = arr[mid]
            high = mid-1
            
    return fl,cl
arr = [80 ,59 ,26 ,46]
print(getFloorAndCeil(arr,28))