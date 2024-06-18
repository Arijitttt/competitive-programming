def k_th_smallest(arr):
    arr.sort()
    k = int(input('enter k_th element: '))
    return arr[k]
arr =[33,22,55,88,9,21,33,44,66]
print('list  is: ',arr)
print('k-th smallest element: ',k_th_smallest(arr))
