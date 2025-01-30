def prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
def check(nums):
    temp = []
    for num in nums:
        if  prime(num):
            temp.append(num)
    return " ".join(map(str,temp))
print(check([1,2,3,4,5,6,7,8,9,10]))