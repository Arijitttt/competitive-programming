def palindrome(str):
    p = ""
    for i in range(len(str)-1,-1,-1):
        p += str[i]
    if str == p:
        print("palindrome")
    else:
        print("not")
str = "abba"
palindrome(str)