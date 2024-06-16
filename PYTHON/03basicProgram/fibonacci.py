# def fibonacci(range):
#     fib_sequence = [0, 1]
#     while len(fib_sequence) < range:
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#     return fib_sequence

# print(fibonacci(10))


def fibonacci(num):
    if num <= 0:
        return []
    if num == 1:
        return [0]
    fib_series = [0,1]
    while(len(fib_series)<num):
        fib_series.append(fib_series[-1]+fib_series[-2])
    return fib_series
print(fibonacci(20))