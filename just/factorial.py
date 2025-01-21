def factorial(num):
    temp = []
    for i in range(1,int(num//2)+1):
        if num % i == 0:
            temp.append(i)
    return " ".join(map(str,temp))

num = int(input("Enter a number: "))
print(factorial(num))