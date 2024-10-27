def prime(num):
    if num<2:
        return False
    for  i in range(2,int(num**0.5)+1):
        if num%i == 0 :
            return False
    return True
def is_googly_prime(N):
    sum_of_digits = sum(int(digit) for digit in str(N))
    print(sum_of_digits)

    return prime(sum_of_digits)

N = 44

if is_googly_prime(N):
    print(f"{N} is a googly prime number.")
else:
    print(f"{N} is not a googly prime number.")