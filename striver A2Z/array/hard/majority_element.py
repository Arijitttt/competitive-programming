def majorityElement(nums):
    n = len(nums)
    freq = {}
    res = []
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for num in freq:
        if freq[num] > (n//3):
            res.append(num)
    return res

print(majorityElement([3,2,3]))