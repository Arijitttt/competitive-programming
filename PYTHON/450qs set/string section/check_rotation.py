def check_rotation(str,n,pivot):
    j=0
    temp1 = ''
    temp2=''
    while(j<pivot):
        temp1+=str[j]
        j=j+1

    while pivot<n:
        temp2+=str[pivot]
        pivot = pivot+1
    new_str = temp2+temp1
    return new_str
s1 = 'abcd'
s2 = 'cdab'
n = len(s1)
left = 0
right = n
pivot = (left+right)//2
new_str = check_rotation(s1,n,pivot)
print(s2,new_str)
if s2==new_str:
    print(f"yes {s1} and {s2} are rotating")
else:
    print("False")