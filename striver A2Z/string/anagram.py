def anagram(s,t):
    if len(s) != len(t):
        return False
    else:
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True

print(anagram("anagram","nagaram"))