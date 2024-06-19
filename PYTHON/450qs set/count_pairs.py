def count_pairs(arr,length):
    key = int(input('enter key value: '))
    temp = 0
    c=0
    for i in range(length):
        for j in range(i+1,length):
            if arr[i]+arr[j]==key:
                c+=1
    return c

arr = [1, 5, 7, 1]
length = len(arr)
print('no of pair is: ',count_pairs(arr,length))
