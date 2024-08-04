#checking perfect square
import math
# num = 9
# sqrt_num = math.sqrt(num)
# if sqrt_num.is_integer():
#     print(1)
# else:
#     print(0)\

def count_sqaures(num):
    c = 0
    for i in range(1,num):
        sqrt_i = math.sqrt(i)
        if sqrt_i.is_integer():
               c += 1
    if not c:
         return -1
    return c
print(count_sqaures(num=9))