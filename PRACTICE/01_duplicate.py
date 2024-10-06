def duplicate(nums):
    freq  = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq = 1
    return freq
nums = [1,2,2,3,4,2,3,3,3,1,4]
print(duplicate(nums))