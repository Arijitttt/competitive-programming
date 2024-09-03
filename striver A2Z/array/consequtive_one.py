def consequtive_ones(nums):
    n = len(nums)
    count , maxCount = 0,0
    for i in range(n):
        if nums[i] == 1:
            count +=1
        else:
            count = 0
        maxCount = max(maxCount,count)

    return maxCount
    

arr = [1,0,1,1,0,1]
print(consequtive_ones(arr))