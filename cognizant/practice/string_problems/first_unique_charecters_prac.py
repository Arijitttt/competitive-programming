from collections import Counter
def first_unique_charecters(s):
    splitted_str = Counter(s)
    for  i,char in enumerate(s):
        if splitted_str[char] == 1:
            return i
    return -1
print(first_unique_charecters('leetcode'))