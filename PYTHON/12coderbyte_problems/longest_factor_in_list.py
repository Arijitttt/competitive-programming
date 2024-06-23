from math import gcd
a = [15, 81, 78]
div = gcd(a[0],a[1])

for i in range(1,len(a)-1):
    div = gcd(div,a[+1])
print(div)


# for i in range(1,x):
#     if x%i==0:
#         print('factors: ',i,end=' ')

# for j in  range(1,len(a)):
#     if a[j]%j==0:
#         temp.append(j)
# print(temp)