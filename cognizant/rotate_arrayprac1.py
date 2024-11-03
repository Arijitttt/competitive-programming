def rotate(nums,d):
    n = len(nums)
    for i in range(d):
        first = nums[0]
        for j in range(n-1):
            nums[j] = nums[j+1]
        nums[n-1] = first
    return nums
print(rotate([1,4,5,2,7,3],3))