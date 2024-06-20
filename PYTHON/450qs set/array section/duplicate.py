a=[22,11,44,55,22,33,11,66,77,88,99,11,55]
c=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:

            print(i,a[i])