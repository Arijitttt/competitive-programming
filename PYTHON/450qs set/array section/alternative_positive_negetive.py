def rearrange_alternate(arr):
    n = len(arr)
    left = 0
    right = n-1

    while left<=right:
        if arr[left]<0 and arr[right]>=0:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        elif arr[left]>=0:
            left+=1
        elif arr[right]<0:
            right-=1


    if left==0 or left==n:
        return arr
    i,j=1,left
    while i<j and j<n:
        arr[i],arr[j]=arr[j],arr[i]
        i+=2
        j+=1
    return arr
arr = [1, 2, 3, -4, -1, 4]
print('after alternating: ',rearrange_alternate(arr))