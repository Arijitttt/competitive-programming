def search_in_rotated_sorted_array(array,target):
    n = len(array)
    count = 0
    for i in range(n):
        if array[i] == target:
            return i
        # elif array[i] != target:
        #     return -1
    # print(count)
    return -1
arr = [4,5,6,7,0,1,2]
target = 0
print(search_in_rotated_sorted_array(arr,target))