def is_prime(num):
    if num <=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
def find_prime(n):
    for i in range(2,int(n/2) + 1):
        if is_prime(i) and is_prime(n-i):
            return f"{n} can be represented as the sum of {i} and {n-i}"
    return f"can not represent"
n = 34
print(find_prime(n))