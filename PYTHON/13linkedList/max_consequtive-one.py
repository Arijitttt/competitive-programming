def max_one(nums):
    l,r = 0,0
    max_count,count = 0,0
    while r <len(nums):
        if nums[r] == 1:
            count += 1
            # max_count = max(max_count,r-l)
        else:
            #max_count = max(max_count,r-l+1)
            count = 0

        max_count = max(max_count,count)
        r += 1

    return max_count
nums = [1,1,0,1,1,1]
print(max_one(nums))