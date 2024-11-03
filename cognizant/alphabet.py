s = list(map(int,input().split()))
temp = []
for  i in range(len(s)):
    temp.append(chr(s[i]))
output = ''.join(temp)
for  i in range(len(s)):
    print(f"{s[i]} - {output[i]}")