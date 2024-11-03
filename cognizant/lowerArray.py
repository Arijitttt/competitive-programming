def lowerArray(nums):
    if not nums:
        return 0
    n = len(nums)
    countArray = [0]*n

    for i in range(n):
        for j in range(i+1,n):
            if nums[i]>nums[j]:
                countArray[i] += 1
    return countArray

print(lowerArray([12, 1, 2, 3, 0, 11, 4]))