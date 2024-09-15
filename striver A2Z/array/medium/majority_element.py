def majority_element(arr):
    count_dict = {}
    n = len(arr)
    for i in range(n):
        if arr[i] in count_dict:
            count_dict[arr[i]] += 1
        else:
            count_dict[arr[i]] = 1

    kwy = count_dict.get
    print(kwy,count_dict)
    max_element = max(count_dict, key=count_dict.get)
    return max_element

print(majority_element([6,5,5]))  # Should print 5