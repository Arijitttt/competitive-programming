def threeSum(nums):
    n = len(nums)
    result = []
    nums.sort()

    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i+1
        right = n-1

        while left<right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.append([nums[i],nums[left],nums[right]])

                while left<right and nums[left] == nums[left+1]:
                    left += 1
                while left<right and nums[right] == nums[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum<0:
                left += 1
            else:
                right -= 1
    return result



            

 

print(threeSum([-1,0,1,2,-1,-4]))