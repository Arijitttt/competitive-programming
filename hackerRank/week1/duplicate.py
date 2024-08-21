def duplicate(string):
    freq = []

    # for num in string:
    #     if num in freq:
    #         freq[num]+=1
    #     else:
    #         freq[num] = 1
    # return freq


    #different way
    for element in string:
        count = string.count(element)
        if count>1:
            freq.append(count)
    return freq


print(duplicate("geekforgeeks"))