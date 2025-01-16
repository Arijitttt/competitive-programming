def sort_by_frequency(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    sorted_array = sorted(freq.items(),key=lambda x:(x[1],x[0]),reverse=True)

    res = []
    for num,frequency in sorted_array:
        res.extend([num]*frequency)
    return " ".join(map(str,res))


print(sort_by_frequency([1,2,44,1,2,5,1,3,3,3,2,5]))