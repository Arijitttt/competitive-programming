def second_large(nums):
    large = float('-inf')
    second_large = float('-inf')
    for num in nums:
        if num > large:
            second_large = large
            large = num
        elif num > second_large and num != large:
            second_large = num
    
    if second_large == float('-inf'):
        return -1
    return second_large
print(second_large([2,2,1,2]))
