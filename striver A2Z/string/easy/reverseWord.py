def reverseWord(s):
    n = len(s)
    l, r = n-1, n-1
    res = []
    
    while l>=0:
        if s[l] == " ":
            
            res.append(s[l+1:r+1])
            r = l-1
        elif l == 0:
            res.append(s[l:r+1])
        l -= 1
    
    return " ".join(res)  # No need to reverse the list, we built it in reverse order

print(reverseWord("The sky is blue"))
