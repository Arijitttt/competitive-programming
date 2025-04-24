from collections import Counter
def first_unique_charecters(s):
    # char_count = Counter(s)
    char_count = {}
    for c in range(len(s)):
        if s[c] in char_count:
            char_count[s[c]]+=1
        else:
            char_count[s[c]] = 1
    for i,char in enumerate(s):
        if char_count[char] == 1:
            return i
    return -1
print(first_unique_charecters('leetcode'))