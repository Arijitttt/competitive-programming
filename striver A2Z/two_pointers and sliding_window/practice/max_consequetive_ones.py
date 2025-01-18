def max_consequetive_ones(nums,k):
    n = len(nums)
    left = 0
    zero_count = 0
    max_count = 0
    for  right in range(n):
        if nums[right] == 0:
            zero_count +=1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -=1
            left += 1
        max_count = max(max_count,right-left+1)
    return max_count
print(max_consequetive_ones([1,1,1,0,0,0,1,1,1,1,0],2))