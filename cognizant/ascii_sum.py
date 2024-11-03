s = input().split()
output = ''.join(s)
sum = 0
for i in range(len(output)):
    sum += ord(output[i])
print(sum)