def subArrays(arr,k):
    n = len(arr)
    max_min = float('-inf')
    for i in range(n-k+1):
        curr_subarray = arr[i:i+k]
        min_val = min(curr_subarray)
        max_min= max(min_val,max_min)
    return max_min
arr = [3, 1, 4, 6, 2, 5]
k = 2
print(subArrays(arr,k))