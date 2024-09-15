def series(arr):
    n = len(arr)
    sum = 0 
    result = []
    for i in range(n):
        sum += arr[i]
        result.append(sum)

    return result
print(series([1,2,3,4]))