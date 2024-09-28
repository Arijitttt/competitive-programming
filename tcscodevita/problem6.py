from itertools import permutations

a,b = list(map(int,input().split())) # 859 900

num = sorted(list(str(a))) #['5','8','9']

permutation = permutations(num)

status = False

for i in list(permutation):
    newnum = ''
    
    for j in i:
        newnum += j
    
    if int(newnum)>b:
        status = True
        break

if status:
    print(newnum)
else:
    print(-1)
