def getLongestSubarray(a,k):
    length = 0
    n = len(a)
    for i in range(n):
        s = 0
        for  j in range(i,n):
            s = s+a[j]

            if s==k:
                length = max(length,j-i+1)
    return length

a = [-1, 1, 1]
k = 1

print(getLongestSubarray(a,k))