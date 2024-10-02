def binary_search(nums, target):
    n = len(nums)
    left = 0
    right = n-1
    mid = (left+right)//2
    while left<= right:
        if nums[mid] == target:
            return mid+1
        elif nums[mid]>target:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left+right)//2
    return -1

print(binary_search([1,2,3,4,5,6,7,8,9,10], 5))