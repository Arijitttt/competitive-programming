#method 1
str = 'abba'
str1 = ''
if str == str[::-1]:
    print('yes')
else:
    print('no')


#method 2
left = 0
right = len(str) - 1

for i in range(len(str)):
    if str[left] != str[right]:
        print('no')

        break
    else:
        str1+=str[right]
        left += 1
        right -= 1
print(str)

# while left < right:
#     str1[left],str1[right]=str[right],str[left]
#     left += 1
#     right -= 1
# print(str1)
# if str==str1:
#     print('palindrome')
# else:
#     print('not palindrome')