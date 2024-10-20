def all_duplicates(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    result = []
    for num in freq:
        if freq[num] > 1:
            result.append(num)
    return result

print(all_duplicates([4,3,2,7,8,2,3,1]))