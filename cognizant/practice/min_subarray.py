def min_subarray(arr,k):
    n = len(arr)
    max_min = float('-inf')
    for i in range(n-k+1):
        subArray = arr[i:i+k]
        min_val = min(subArray)
        max_min = max(max_min,min_val)
    return max_min
arr = [3, 1, 4, 6, 2, 5]
k = 2
print(min_subarray(arr,k))