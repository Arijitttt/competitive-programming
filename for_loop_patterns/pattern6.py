for i in range(5,0,-1):
    for j in range(5,0,-1):
        if j >= i:
            print(j,end=' ')
        else:
            print(i,end=' ')
    print()
'''
5 5 5 5 5 
5 4 4 4 4
5 4 3 3 3
5 4 3 2 2
5 4 3 2 1
'''