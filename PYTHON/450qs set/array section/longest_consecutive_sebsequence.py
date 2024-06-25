def logest_sonsecutive_subsequence(arr):
    n = len(arr)
    arr.sort()
    print(arr)
    count = 1
    max_count = 1
    for i in range(1,n):
        if arr[i]==arr[i-1]:
            continue
        elif arr[i]==arr[i-1]+1:
            count+=1
        else:
            max_count = max(max_count,count)
            count = 1
    max_count = max(max_count,count)

    return max_count
arr = [1,9,3,10,4,20,2]
print(logest_sonsecutive_subsequence(arr))