#factors
def getFactors(num):
    factors = []
    for i in range(1,num):
        if(num%i==0):
            factors.append(i)

    return factors
num = 28
print('factors are : ',getFactors(num))