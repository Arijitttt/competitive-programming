def TwoSum(nums,target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff],i]
        seen[nums[i]] = i

    return []
print(TwoSum([3,2,4],6))