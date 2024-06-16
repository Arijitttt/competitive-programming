# def Prime(first,last):
#     for num in range(first,last+1):
#         print('index: ',num)
#         if num > 1:
#             for i in range(2,num):
#                 if (num % i) == 0:
#                     break
#                 else:
#                     print(num)
#                     break
# Prime(10,20)

def Prime(fist,last):
    track=[]
    for num in range(fist,last):
        if num > 1:
            for i in range(2,num):
                if num%i==0  :
                    break
                else:
                    track.append(num)
                    print(num)
                    break
    print("length:",len(track))
Prime(30,60)