def subStrCount(s):
    if len(s) ==0:
        return []
    elif len(s) == 1:
        return [s]
    else:
        output = []
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                output.append(s[i:j])
    return output+subStrCount(s[1:])

s = 'geeksforgeeks'
print(subStrCount(s))