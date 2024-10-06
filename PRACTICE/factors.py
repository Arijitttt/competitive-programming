def factors(n):
    for i in range(1,n):
        if n%i == 0:
            print(i,end=' ')
    else:
        return -1
    
factors(5)