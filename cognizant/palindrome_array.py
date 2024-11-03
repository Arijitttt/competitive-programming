def isPalindrome(num):
    temp = str(num)
    if temp == temp[::-1]:
        return 1
    return 0

def palindromic_array(nums):
    if not  nums:
        return 0
    for num in nums:
        if not isPalindrome(num):
            return False
    return True
if palindromic_array([121,131,202,121]):
    print("palindrome")
else:
    print("not palindrome")