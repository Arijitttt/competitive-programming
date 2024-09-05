def twoSum(nums, target):
    n = len(nums)
    left = 0
    right = n - 1
    nums.sort()
    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1    
nums = [3,2,4]
target = 6
print(twoSum(nums, target))

