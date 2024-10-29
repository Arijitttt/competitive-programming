def move_zeros(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            for j in range(i+1,len(arr)):
                if arr[j] != 0:
                    arr[i],arr[j] = arr[j],arr[i]
                    break
    print(arr)

print(move_zeros([0,1,0,3,12]))