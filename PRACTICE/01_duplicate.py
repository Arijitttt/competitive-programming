def duplicate(nums):
    freq = {}
    for num in  nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for num in freq:
        print(num,':',freq[num])
        # if freq[num]>1:
        #     print(num)

nums = [1,3,4,2,2]
duplicate(nums)