def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2

        left = nums[:mid]
        right = nums[mid:]

        merge_sort(left)
        merge_sort(right)

        i=0
        j = 0
        k = 0

        while i<len(left) and j < len(right):
            if left[i]<right[j]:
                nums[k]=left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k+= 1
        
        while i<len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
    return nums

print(merge_sort([1,3,5,7,9,2,4,6,8,10,11]))