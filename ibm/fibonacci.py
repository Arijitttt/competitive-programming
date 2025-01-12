n = 5
fib = [0,1]
while len(fib) <= n:
    fib.append(fib[-1]+fib[-2])

print(fib)