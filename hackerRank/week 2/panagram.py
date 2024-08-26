def panagram(s):
    s= s.lower()
    for letter in range(ord('a'),ord('z')+1):
        temp = chr(letter)
        if temp not in s:
            return 'not panagram'
    return 'panagram'



s = 'The quick brown frogs jumps over the lazy dog'
print(panagram(s))