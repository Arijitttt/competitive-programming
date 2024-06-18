def max_subArray_sum(arr):
    if not arr:
        return 0
    max_ending_here = arr[0]
    max_so_far=arr[0]

    for i in arr[1:]:
        max_ending_here = max(i,max_ending_here+i)
        max_so_far=max(max_so_far,max_ending_here)

        return max_so_far
arr = [33,11,22,55,77,22,11,44,22]
print('max sub array sum: ',max_subArray_sum(arr))