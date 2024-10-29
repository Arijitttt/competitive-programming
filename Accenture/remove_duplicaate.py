def remove_duplicate(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    # print(freq)
    output =  list(freq.keys())
    return ''.join(map(str,output))
    # return str(output)
print(remove_duplicate([1,1,1,2,2,3]))