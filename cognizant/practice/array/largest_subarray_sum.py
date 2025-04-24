def largest_subarray_sum(arr):
    current_max = arr[0]
    max_so_far = arr[0]
    for num in arr[1:]:
        current_max = max(current_max+num,num)
        max_so_far = max(current_max,max_so_far)
    return max_so_far
print(largest_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))