a=[33,11,66,44,88,99]
max = a[0]
min = a[0]
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
    if a[i]<min:
        min=a[i]
print(max,min)

