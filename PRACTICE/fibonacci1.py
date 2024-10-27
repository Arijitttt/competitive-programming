def fibonacci(n):
    fib = [0,1]
    while len(fib)<n+1:
        fib.append(fib[-1]+fib[-2])
    return fib

print(fibonacci(5))