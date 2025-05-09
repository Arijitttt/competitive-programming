def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num,num+current_sum)
        max_sum = max(max_sum,current_sum)
    return max_sum
print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))