def all_permurtations(arr):
    res = []
    if len(arr) == 1:
        return [arr]
    for i in range(len(arr)):
        for j in all_permurtations(arr[:i] + arr[i+1:]):
            res.append([arr[i]] + j)
    return res
print(all_permurtations([1,2,3]))