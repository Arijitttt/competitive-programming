def move_zeros(nums):
    n = len(nums)

    # for i in range(n):
    #     if nums[i] == 0:

    #         for j in range(i+1, n):
    #             if nums[j] != 0:
    #                 nums[i], nums[j] = nums[j], nums[i]
    #                 break

    # print(nums)

    #another optimal way
    left= 0
    for right in range(n):
        if nums[right] != 0:
            nums[right],nums[left] = nums[left],nums[right]
            left += 1
    print(nums)
nums = [0,1,0,3,12]

print(move_zeros(nums))