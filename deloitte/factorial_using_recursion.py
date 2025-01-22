def factorial_using_recursion(num):
    if num == 1:
        return 1
    return num*factorial_using_recursion(num-1)

print(factorial_using_recursion(5))