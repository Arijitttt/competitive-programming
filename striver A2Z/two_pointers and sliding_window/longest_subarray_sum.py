def longest_subarray_sum(nums):
    maxSum=current_sum=nums[0]
    n=len(nums)
    for r in range(1,n):
        current_sum = max(nums[r],current_sum+nums[r])
        maxSum = max(maxSum,current_sum)
    return maxSum
nums = [5,4,-1,7,8]
print(longest_subarray_sum(nums))  # Output: 23
