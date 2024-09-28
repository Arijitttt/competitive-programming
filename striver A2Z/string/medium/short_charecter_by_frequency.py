def short_charecter_by_frequency(s): #tree -> eert/eetr
    freq ={}
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    sorted_chars = sorted(freq.items(),key = lambda x :(-x[1],x[0]))
    result = ''.join([char * count for char, count in sorted_chars])

    return result
        
print(short_charecter_by_frequency("tree"))