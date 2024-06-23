def zero_sum_subarray(arr):

    cumpulative_sum_set = set()

    cumpulative_sum = 0

    for num in arr:
        cumpulative_sum += num

        if cumpulative_sum == 0 or cumpulative_sum in cumpulative_sum_set:
            return True

        cumpulative_sum_set.add(cumpulative_sum)
        print(cumpulative_sum)

        print(cumpulative_sum_set)
        print()
    return False
arr = [4,2,0,1,6]

print(zero_sum_subarray(arr))



