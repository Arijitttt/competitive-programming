def counting_sort(arr):
    range = max(arr)
    void_array  = [0]*(range+1)
    for num in arr:
        #void_array[num] += 1
        count = arr.count(num)
        void_array[num] = count
    return void_array
arr = [1, 1, 3, 2, 1]
print(counting_sort(arr))