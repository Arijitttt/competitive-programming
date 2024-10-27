
def round_number(num):
    while num >=10:
        num = square_addition(num)
    print(num)
def square_addition(num):
    temp = 0
    while num > 0:
        last_digit =num%10
        temp=temp+ last_digit**2
        num = num//10
    return temp
round_number(11)