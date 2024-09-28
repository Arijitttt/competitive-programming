n = int(input()) #no. of trains
arr = []
dep = []

for  i in range(n):
    a,d  = map(int,input().split()) #2 4
    
    d += a
    arr.append(a)
    dep.append(d)