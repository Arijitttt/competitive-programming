def count_inversion(arr):
    if not arr:
        return []
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                count = count+1
                # arr[i], arr[j] = arr[j], arr[i]

    return count
arr = [1,4,2,6,3,1,4,2,7,5]

print('count inversion is: ',count_inversion(arr))