def missing_number(nums):
    n = len(nums)
    s1 = n*(n+1)//2
    s2 = sum(nums)
    diff = s1 - s2
    return diff

nums = [3,0,1]
print(missing_number(nums))