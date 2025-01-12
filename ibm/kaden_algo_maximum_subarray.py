def maximum_subarray(arr):
    if not arr:
        return 0
    max_ending_here,max_so_far = arr[0],arr[0]
    for num in arr[1:]:
        max_ending_here = max(num,max_ending_here+num)
        max_so_far = max(max_so_far,max_ending_here)
    return max_so_far
print(maximum_subarray([2,5,7,1,5,4]))