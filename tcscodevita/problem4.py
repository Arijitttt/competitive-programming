val = list(map(int,input().split()))
odd,even = 0,0
for i in range(0,len(val),2):
    even += val[i]
for j in range(1,len(val),2):
    odd += val[i]

print(max(odd,even))