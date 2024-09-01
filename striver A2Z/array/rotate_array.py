def rotate_array(nums,k):
    n = len(nums)
    nums[:] =nums[n-k:]+ nums[:n-k]

    #merge 2 arrays


    print(nums)


nums = [1,2,3,4,5,6,7]
k = 3

rotate_array(nums,k)