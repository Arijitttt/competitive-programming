def palindrome(num):
    if num<0:
        return 'Invalid Input'
    num = str(num)
    arr = [1,2,1,3]
    print(arr)
    arr.reverse()
    print(arr)
    rev_num = num[::-1]
    if num == rev_num:
        return True
    else:
        return False
    
if(palindrome(121)):
    print('palindrome')
else:
    print('not')