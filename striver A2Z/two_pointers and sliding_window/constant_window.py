def constant_window(arr,k): #k = window size
    n = len(arr)
    if k > n:
        return None
    l = 0
    r = k
    window_sum=maxSum = sum(arr[:k])
    while(r < n-1):
        window_sum = window_sum - arr[l] + arr[r]
        l += 1
        r += 1
        maxSum = max(maxSum,window_sum)

    print(maxSum)
arr  = [-1,2,3,3,4,5,-1]
constant_window(arr,4)