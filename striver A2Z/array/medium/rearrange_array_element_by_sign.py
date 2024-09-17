def rearrange_array_element_by_sign(nums):
    posIndex,negIndex = 0,1
    n = len(nums)
    res = [0]*n

    for num in nums:
        if num < 0:
            res[negIndex] = num
            negIndex += 2
        else:
            res[posIndex] = num
            posIndex += 2
    return res
print(rearrange_array_element_by_sign([3,1,-2,-5,2,-4]))