def palindrome(num):
    temp = num
    rev = 0
    while num > 0:
        last_digit = num % 10
        rev = rev * 10 + last_digit
        num = num // 10
    if temp == rev:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")