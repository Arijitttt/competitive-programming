import math
def square_free_number(n):
    count = 0
    for i in range(2,n):
        if n%i == 0:
           sq = math.sqrt(i)
           if not sq.is_integer():
               count += 1
            
    return count


n = int(input('enter the number : '))
print(square_free_number(n))
