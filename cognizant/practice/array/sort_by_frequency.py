def sort_by_freq(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    sorted_freq = sorted(freq.items(),key= lambda x:(x[1],x[0]),reverse=True)
    result1,result2 = [],[]
    for num,frequency in sorted_freq:
        result1.extend([num]*frequency) #3 3 3 2 2 2 1 1 1 5 5 44
    for num in sorted_freq:
        result2.append(num[0]) #3 2 1 5 44
    #result = list(set(result))
    return ' '.join(map(str,result2))
print(sort_by_freq([1,2,44,1,2,5,1,3,3,3,2,5]))