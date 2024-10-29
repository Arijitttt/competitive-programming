def kaden_algo(nums):
    max_so_far,max_ending_here = nums[0],nums[0]
    for  num in nums[1:]:
        max_ending_here = max(num,max_ending_here+num)
        max_so_far = max(max_ending_here,max_so_far)
    return max_so_far
print(kaden_algo([-2,1,-3,4,-1,2,1,-5,4]))