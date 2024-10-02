import math
print(math.gcd(6,60))

#or

num1 = 6
num2 = 60
gcd = 1
for i in range(1,min(num1,num2)+1):
    if num1%i == 0 and num2%i == 0:
        gcd = i
print(gcd)

#lcm
print(math.lcm(10,15))