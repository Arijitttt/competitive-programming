def sliding_window_practice(arr,k):
    maxSum =l=r=length =  0
    n = len(arr)
    subArray = []
    while r<n:
        maxSum =maxSum+arr[r]
        while maxSum>k:
            maxSum = maxSum -arr[l]
            l = l+1
        if maxSum<k:
            length = max(length,r-l+1)
            subArray = arr[l:r+1]
        r += 1
    return length,subArray
print(sliding_window_practice([5,4,-1,7,8],14))