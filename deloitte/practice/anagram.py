s1 = 'HELLO'
s2 = 'EHLLO'
if sorted(s1.lower()) == sorted(s2.lower()):
    print('anagram')
else:
    print('not anagram')