def Sum_of_Odd_Integers(arr,n):
    addition = 0
    for i in range(n):
        if arr[i] % 2 != 0:
            addition += arr[i]
    print(addition)
arr = [1,2,5,7,10,12,11,1]
n = len(arr)
Sum_of_Odd_Integers(arr,n)