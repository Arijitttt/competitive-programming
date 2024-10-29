def rotate(nums,k):
    n = len(nums)
    k = k%n
    nums[:] = nums[n-k:] + nums[:n-k]
    print(nums)

nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums,k)