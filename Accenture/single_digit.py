#given a number N. your task is to make N a single digit number by performing the following operation:

# if N is ODD make it floor(N/2)
# if N is even make it floor((N-2)/2)
# If N is already a single digit bring it as it is

n = 10
while n>9:
    if n%2==0:
        n = (n-2)//2
    else:
        n = n//2
print(n)