def sliding_window(arr,k):
    l = r= maxSum = maxLen= 0
    n = len(arr)
    temp = []
    while(r<n):
        maxSum = maxSum + arr[r]
        while maxSum > k:
            maxSum = maxSum - arr[l]
            l = l+1
        if maxSum<=k:
            maxLen = max(maxLen,r-l+1)
            temp = arr[l:r+1]
        r += 1
    print(f"length = {maxLen},subarray={temp} sum = {maxSum}")
arr = [5,4,-1,7,8]
k = 14
sliding_window(arr,k)