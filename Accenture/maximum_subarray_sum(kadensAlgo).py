def maximum_subarray_sum(nums):
    if not nums:
        return 0
    max_ending_here,max_so_far = nums[0],nums[0]
    for num in nums[1:]:
        max_ending_here = max(num,max_ending_here+num)
        max_so_far = max(max_so_far,max_ending_here)
    return max_so_far
print(maximum_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))