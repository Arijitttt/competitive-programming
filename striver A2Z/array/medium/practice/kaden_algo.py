def kaden_algo(nums):
    n = len(nums)
    max_sum = nums[0]
    curr_sum = nums[0]
    for i in range(1,n):
        curr_sum = max(nums[i],nums[i]+curr_sum)
        max_sum = max(max_sum,curr_sum)
    return max_sum
print(kaden_algo([-2,1,-3,4,-1,2,1,-5,4]))