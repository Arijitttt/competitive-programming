def square_sort(arr):
    n = len(arr)
    l = 0
    r = n-1
    res = []
    while l <= r:
        if abs(arr[l])> abs(arr[r]):
            res.append(arr[l]**2)
            l += 1
        else:
            res.append(arr[r]**2)
            r -= 1
    return res[::-1]
print(square_sort([-4, -1, 0, 3, 10]))
