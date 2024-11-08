def countSubstring(s,k):
    n = len(s)
    count = 0
    for i in range(n):
        distinc_chars = set()
        for j in range(i,n):
            distinc_chars.add(s[j])
            if len(distinc_chars) == k:
                count += 1
            elif len(distinc_chars) > k:
                break
    return count

print(countSubstring('aba',2))