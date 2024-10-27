def remove_duplicates(nums):
    freq = {}
    temp = []
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for num in freq:
        temp.append(freq[num])
    for i in range(len(nums)):
        nums[i] = temp[i]
        return len(temp)
 
print(remove_duplicates([1,1,2]))