def largest_element(nums):
    if not nums:
        return 0
    m = nums[0]
    for num in nums[1:]:
        if num>m:
            m = num
    return m
print(largest_element([1,2,3,4,5,6,3,1]))