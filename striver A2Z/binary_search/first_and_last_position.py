def first_and_last_position(nums,target):
    if not nums:
        return [-1,-1]
    def leftmost():
        left,right = 0,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>=target:
                right = mid - 1
            else:
                left = mid + 1
        return left
    def rightmost():
        left,right = 0,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>target:
                right  = mid -1
            else:
                left = mid+1
        return right
    leftmost = leftmost()
    rightmost = rightmost()
    if leftmost > rightmost:
        return [-1,-1]
    return [leftmost,rightmost]

nums = [5,7,7,8,8,10]
target = 8
print(first_and_last_position(nums,target))