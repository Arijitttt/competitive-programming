def missing_repeating(arr,n):
    repeating = -1
    missing = -1
    frequency = [0]*(n+1)
    for num in arr:
        frequency[num] += 1
    for i in range(1,n+1):
        if frequency[i] == 0:
            missing = i
        elif frequency[i] > 1:
            repeating = i
    return [repeating,missing]
arr = [2,2]
n = len(arr)
print(missing_repeating(arr,n))