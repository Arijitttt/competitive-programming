pwd = '101011'
count = 0
for i in range(len(pwd)):
    if pwd[i] == '0':
        count += 1
print(count)