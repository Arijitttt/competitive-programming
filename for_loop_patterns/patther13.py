for i in range(1,6):
    for k in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,2*i):
        if i>1 and i==j:
            print("0",end=' ')
        else:
            print("1",end=' ')
    print()
'''     1 
      1 0 1
    1 1 0 1 1
  1 1 1 0 1 1 1
1 1 1 1 0 1 1 1 1'''