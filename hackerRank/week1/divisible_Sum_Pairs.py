def divisibleSumPairs(n,k,ar):
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i]+ar[j])%k == 0:
                c+=1
    return c

ar = [1,2,3,4,5,6]
print(divisibleSumPairs(len(ar),5,ar))