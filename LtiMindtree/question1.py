def average_of_multiples(n,p):
    sum = 0
    for i in range(1,p+1):
        sum = sum+(n*i)
    print(sum//p)


average_of_multiples(9,5)