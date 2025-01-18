def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num %i == 0:
            return False
    return True
def good_numbes(arr):
    for i in range(len(arr)):
        if i%2 == 0 and arr[i]%2 ==0:
            pass
        else:
            return False
        

