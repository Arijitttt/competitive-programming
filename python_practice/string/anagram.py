def anagram(str1,str2):
    if len(str1) != len(str2):
        print("length mismatched")
        return
    else:
        str1 = sorted(str1)
        str2 = sorted(str2)
        # print(str1,'\t',str2)
        if str1 == str2:
            print("anagram")
        else:
            print("not anagram")
str1 = 'silent'
str2 = 'listen'

anagram(str1,str2)