def consequtive_one(arr,k):
    n = len(arr)
    zero_count = 0
    left = 0
    max_ones = 0
    for right in range(n):
        if arr[right] == 0:
            zero_count += 1
            while zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1
        max_ones = max(max_ones,right-left+1)
    return max_ones
print(consequtive_one([1,1,1,0,0,0,1,1,1,1,0],2))