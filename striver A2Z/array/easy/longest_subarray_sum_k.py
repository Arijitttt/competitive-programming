def longest_subarray_sum_k(arr,n, k):
    l ,r = 0,0
    Sum=arr[0]
    maxLen = 0
    # temp = []
    while r<n:
        while l<=r and Sum>k:
            Sum = Sum - arr[l]
            l += 1
        if Sum==k:
            maxLen = max(maxLen,r-l+1)
            # temp = arr[l:r+1]
        r += 1
        if r<n:
            Sum = Sum + arr[r]
    return maxLen
arr = [2, 3, 5, 1, 9]
print(longest_subarray_sum_k(arr,len(arr), 10))