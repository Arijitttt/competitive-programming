def max_consequetive_ones(nums,k):
    left = 0
    max_ones = 0
    zero_count = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        max_ones = max(max_ones,right-left+1)
    return max_ones
print(max_consequetive_ones([1,1,1,0,0,0,1,1,1,1,0],2))
    