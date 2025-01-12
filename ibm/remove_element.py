def remove_element(nums,index):
    base = 0
    for num in range(len(nums)):
        if nums[num] == nums[index]:
            left,right = num-1,num+1
            while left >=0 and nums[left] == nums[index]:
                nums.replace(nums[left],'')
                left -= 1
            while right < len(nums) and nums[right] == nums[index]:
                nums.replace(nums[right],'')
                right += 1

    return nums
print(remove_element('baabacaa',5))

