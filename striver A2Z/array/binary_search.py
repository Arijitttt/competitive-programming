def binary_search(nums, target):
    n = len(nums)
    low  = 0
    high = n-1
    mid = (low+high)//2
    while low<=high:
        if nums[mid] == target:
            return mid
        elif nums[mid]>target:
            high = mid - 1
        else:
            low = mid + 1
        mid = (low+high)//2
    return -1


nums = [-1,0,3,5,9,12]
target = 9

print(binary_search(nums, target))