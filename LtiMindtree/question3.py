def question3(N):
    sum = 0
    for i in range(2,N+1,2):
        if i%2 == 0:
            
            sum = sum+i
    return sum
print(question3(6))