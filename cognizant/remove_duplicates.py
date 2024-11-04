def remove_duplicates(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    output = list(freq.keys())
    return ' '.join(map(str,output))
print(remove_duplicates([2,3,1,2,3,4,1,5,6,3,12]))