str = 'hello from python'
#finding space
str1 = []
for i in range(len(str)):
    if(str[i]==' '):
        break
    str1.append(str[i])

print(str1)