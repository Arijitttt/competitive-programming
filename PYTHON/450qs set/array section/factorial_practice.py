def factorial_practice(n):
    resultt = []
    fact = 1
    for i in range(1,n+1):
        fact *= i
        #resultt.insert(0,fact)
    while fact>0:
        a = fact%10
        resultt.insert(0,a)
        fact //= 10
    return resultt

n=6
print(factorial_practice(n))