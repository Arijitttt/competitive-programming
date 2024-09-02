def union_of_two_arrays(arr1, arr2,n,m):
    merge = arr1 + arr2
    merge = list(set(merge))
    merge.sort()
    print(merge)

arr1 = [1,2,3,4,5]
arr2 = [1,2,3,6,7]

union_of_two_arrays(arr1,arr2,len(arr1),len(arr2))