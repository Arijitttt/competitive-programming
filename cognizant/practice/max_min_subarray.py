def max_min_subarray(arr,k):
    n = len(arr)
    max_val = float('-inf')
    for  i in range(n-k+1):
        current_subArray = arr[i:i+k]
        min_val = min(current_subArray)
        max_val = max(max_val,min_val)
    return max_val
print(max_min_subarray([1,2,3,4,5],3))