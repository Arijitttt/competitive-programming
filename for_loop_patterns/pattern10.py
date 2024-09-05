for i in range(1,6):
    for k in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,2*i):
        if i>1 and i == j:
            print(" ",end=' ')
        else:
            print('*',end=' ')
    print()

'''      * 
      *   *
    * *   * *
  * * *   * * *
* * * *   * * * *'''