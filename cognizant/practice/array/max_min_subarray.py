def max_min_subarray(arr,k):
    n = len(arr)
    max_val = float('-inf')
    for i in range(n-k+1):
        cuurent_subaaray = arr[i:i+k]
        min_val = min(cuurent_subaaray)
        max_val = max(max_val,min_val)
    return max_val
arr = list(map(int,input().split()))
k = int(input())
print(max_min_subarray(arr,k))