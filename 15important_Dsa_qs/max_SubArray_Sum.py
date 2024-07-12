def maximum_subarray_sum(arr):
    if not arr:
        return 0
    max_sum = arr[0]
    max_so_far = arr[0]

    for num in arr[1:]:
        max_sum = max(num,max_sum+num)
        max_so_far = max(max_so_far,max_sum)
    return max_so_far
arr = [1, 2, 3, -2, 5]
print(maximum_subarray_sum(arr))