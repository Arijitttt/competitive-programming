def fibonacci(range):
    temp = [0,1]
    while len(temp)<range:
        temp.append(temp[-1] + temp[-2])
    return temp
print(fibonacci(5))