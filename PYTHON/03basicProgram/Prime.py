def Prime(first,last):
    for num in range(first,last+1):
        print('index: ',num)
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
                else:
                    print(num)
                    break
Prime(10,20)

