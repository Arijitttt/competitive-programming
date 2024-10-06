def palindrome(num):
    # rev_num = reversed(num)
    # if list(num) == list(rev_num):
    #     return "palindrome"
    # else:
    #     return False
    rev_num = num[::-1]
    if num == rev_num:
        return True
    else:
        return False
    
print(palindrome(input()))