import math
num1 = 6
num2 = 60
print(math.gcd(num1,num2))

gcd = 0
for i in range(1,min(num2,num1)+1):
    if num1%i == 0 and num2%i == 0:
        gcd = i
print(gcd)

#lcm
print(math.lcm(num1,num2))