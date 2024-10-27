s = 'aAnThe'
res = []
for  i in range(len(s)):
    if 'a'<=s[i]<='z':
        res.append(s[i].upper())
    else:
        res.append(s[i].lower())
print(res)
output = ''.join(res)
print(output)