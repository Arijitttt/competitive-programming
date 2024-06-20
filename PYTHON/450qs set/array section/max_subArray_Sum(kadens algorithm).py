def max_subarray_sum(arr):
    if not arr:
        return 0

    max_ending_here = arr[0]
    max_so_far = arr[0]

    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Examples
arr1 = [1, 2, 3, -2, 5]
arr2 = [-1, -2, -3, -4]
arr3 = [5, 4, 7]

print(max_subarray_sum(arr1))  # Output: 9
print(max_subarray_sum(arr2))  # Output: -1
print(max_subarray_sum(arr3))  # Output: 16
