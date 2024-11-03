def alternate_elemenrts(nums):
    for i in range(len(nums)):
        if i%2 == 0:
            print(nums[i],end=' ')
alternate_elemenrts([1,2,3,4,5])