#find factors of a number
def find_factors(num):
    if num == 0:
        return 'No Factors'
    num = abs(num)
    for i in range(1,num+1):
        if num%i == 0:
            print(i,end = ' ')

find_factors(-55)