def isPrime(n):
    x = n//2
    while x>1:
        if n%x == 0:
            return False
        x -= 1
    return True

d,p = map(int,input().split())
n = int(d/p)

count  = 0
for  i in range(2,n):
    if isPrime(i): #2
        prime_time = True
        for j in range(p): #p = 2
            num = i+j*n #2+0*12 = 2
            if not isPrime(num):
                prime_time = False
                break
        if prime_time:
            count += 1

print(count)
