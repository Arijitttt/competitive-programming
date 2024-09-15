def remove_duplicates(nums):
    freq = {}
    temp = []
    n = len(nums)
    for i in range (n):
        if nums[i] in freq:
            freq[nums[i]] += 1
        else:
            freq[nums[i]] = 1
    for num in freq:
        temp.append(num)
    for i in range(len(temp)):
        nums[i] = temp[i]
    print(nums)
    return len(temp)
   
print(remove_duplicates(
    [1,1,2]
))
