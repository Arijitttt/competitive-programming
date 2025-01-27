num  = 123
sum_ = 0
p = num
while num > 0:
    t = num%10
    sum_ = sum_+ t
    num = num//10
res = p // sum_
print(res)