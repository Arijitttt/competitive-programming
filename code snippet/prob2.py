def valid(S):
    n = len(S)

    if S[0] != 'a':
        return False
    i=0
    while i<n:
        if S[i] == 'a':
            i += 1
        elif i+1 <n and S[i:i+2] == 'bb':
            i += 2
            if i<n and S[i]!= 'a' and i+1 < n and S[i:i+2] != 'bb':
                return False
        else:
            return False
    return True
print(valid('aabbaa')) 