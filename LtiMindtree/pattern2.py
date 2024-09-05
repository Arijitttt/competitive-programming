n= 1
for i in range(1,6):
    for j in range(1,6):
        if j<=i:
            print(n,end=' ')
            n+=1
            if i-j>0:
                print("*",end=' ')
    print()