def supirior_element(arr):
    n = len(arr)
    m,sup_ele = 0,0
    for i in range(n-1,-1,-1):
        if arr[i]>m:
            m = arr[i]
            sup_ele += 1
    print(sup_ele)
arr = [7,9,5,2,8,7]
supirior_element(arr)