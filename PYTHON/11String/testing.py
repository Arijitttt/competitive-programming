str = 'ghijklmnop'
for i in range(len(str)):
    next_char = chr(ord(str[i])+1)


    if next_char in 'aeiou':
        # next_char = chr(ord(next_char)-32)
        next_char = next_char.upper()
    print(next_char,end=' ')

    # if next_char == 'o' or next_char == 'a' or next_char == 'e' or next_char == 'i' or next_char == 'u' :
    #     chr(ord(next_char[i])-32)
    # print(next_char,end=' ')
# print()
# str1 = 'abcd'
# for i in range(len(str1)):
#     print(chr(ord(str1[i])-32))