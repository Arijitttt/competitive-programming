def rotation(str,n,pivot):
    temp1 = ''
    temp2 = ''
    temp3 = ''
    if pivot == 0:
        return str
    else:
        for i in range(0,pivot+1):
            temp1 += str[i]


        for j in range(pivot+1,n):
            temp2+=str[j]
        temp3 = temp2+temp1

        return temp3

str = 'ABCD'
str2= 'ACBD'
n = len(str)
start = 0
end = n-1
pivot  = (start+end)//2
temp3 = rotation(str,n,pivot)
if temp3 == str2:
    print("yes,rotating")
else:
    print("no,not rotating")
