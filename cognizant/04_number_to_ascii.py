#ip =list(map(int,input().split()))

numbers = list(map(int,input().split()))
for number in numbers:
    temp = chr(number)
    print(number,'-',temp,end=' ')