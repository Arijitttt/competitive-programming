def second_smallest(arr,n):
    small = float('inf')
    second_small = float('inf')
    n = len(arr)
    for i in range(n):
        if arr[i] < small:
            second_small = small
            small = arr[i]
        elif arr[i]<second_small and arr[i]!= small:
            second_small = arr[i]
    if second_small == float('inf'):
        return -1
    return second_small


arr = [10,101,24,3]
n = len(arr)
print(second_smallest(arr,n))