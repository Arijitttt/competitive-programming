def second_largest(arr,n):
    large = float('-inf')
    second_large = float('-inf')

    for i in range(n):
        if arr[i] > large:
            second_large = large
            large = arr[i]
        elif arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
        
    if second_large == float('-inf'):
        return -1
    return second_large

print(second_largest([3,2,6,1],4))