def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    print(cleaned)
    return cleaned == cleaned[::-1]
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))