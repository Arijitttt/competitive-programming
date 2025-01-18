def subarray_sum(arr,target_sum):
    start = 0
    current_sum = 0
    n = len(arr)
    for end in range(n):
        current_sum += arr[end]
        while current_sum > target_sum and start <= end:
            current_sum -= arr[start]
            start += 1
        if current_sum == target_sum:
            return start,end
    return None
arr = [1, 4, 20, 3, 10, 5]
target_sum = 33
print(subarray_sum(arr,target_sum))