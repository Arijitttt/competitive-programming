def mini_max_sum(arr):
    if not arr:
        return 0
    minimum = min(arr)
    maximum = max(arr)
    m = 0
    for num in arr[:]:
        m = m+num
    min_result = m -maximum
    max_result = m - minimum
    return min_result,max_result
arr = [1,3,5,7,9]
print(mini_max_sum(arr))

