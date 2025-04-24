def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def checking_prime(arr,n):
    res = []
    for num in arr:
        if prime(num):
            res.append(num)
    return " ".join(map(str,res))
print(checking_prime([3,5,6,8,10],5))