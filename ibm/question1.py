#check integer
arr = list(map(str,input().split()))
integer_add = []
for i in arr:
    if i.isdigit():
        integer_add.append(int(i))
print(integer_add)
temp = {}
for num in integer_add:
    if num in temp:
        temp[num]+=1
    else:
        temp[num] = 1
for num in temp:
    if temp[num] > 1:
        print(num,'',temp[num])

x= list(temp.keys())
print(x)


#print(all(i.isdigit() for i in arr))