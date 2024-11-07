def threeSum(nums):
    result = []
    nums.sort()
    n  = len(nums)

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets = [nums[i],nums[j],nums[k]]

                    if triplets not in result:
                        result.append(triplets)
    
    return result

print(threeSum([-1,0,1,2,-1,-4]))