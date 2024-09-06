def remove_vowel(s):
    for i in s:
        if i in 'aeiouAEIOU':
            s = s.replace(i,'')
    return s
s = 'gag'
print(remove_vowel(s))