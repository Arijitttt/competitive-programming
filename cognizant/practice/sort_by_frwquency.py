def sort_by_frequency(arr):
    freq = {}
    for  i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    # return list(freq.keys())
    sorted_keys = sorted(freq.items(),key=lambda x:(x[1],x[0]),reverse=True)
    result = []
    for num,frequency in sorted_keys:
        result.extend([num]*frequency)
    return " ".join(map(str,result))

print(sort_by_frequency([1,2,44,1,2,5,1,3,3,3,2,5]))