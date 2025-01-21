def armstrong(num):
    #armstrong
    temp = num
    rev = 0
    while num > 0:
        last_digit = num % 10
        rev = rev + (last_digit**3)
        num = num // 10
    if temp == rev:
        return True
    else:
        return False
    
num = int(input("Enter a number: "))
if armstrong(num):
    print("Armstrong")
else:
    print("Not Armstrong")