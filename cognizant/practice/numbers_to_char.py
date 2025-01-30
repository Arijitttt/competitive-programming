numbers = list(map(int,input().split()))
for number in numbers:
    c = chr(number)
    print(f'{number} -{c}')