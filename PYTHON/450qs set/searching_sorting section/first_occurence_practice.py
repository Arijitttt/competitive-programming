def first_last_occurence(arr,n,x):
    def first_occurence(arr,low,high,x):
        if high >= low:
            mid = (low+high)//2
            if (mid == 0 or x>arr[mid-1]) and arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return first_occurence(arr,low,mid-1,x)
            else:
                return first_occurence(arr,mid+1,x)
        return -1
    def last_occurence(arr,low,high,x):
        if high >= low:
            mid = (low+high)//2
            if(mid == n-1 or x<arr[mid+1]) and x==arr[mid]:
                return mid
            elif x>arr[mid]:
                return last_occurence(arr,mid+1,high,x)
            else:
                return last_occurence(arr,low,mid-1,x)
        return -1
    first = first_occurence(arr,0,n-1,x)
    if first == -1:
        return -1
    last = last_occurence(arr,0,n-1,x)
    return first,last
arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
print(first_last_occurence(arr, len(arr), 5))