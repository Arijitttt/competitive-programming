def duplicate(arr,n):
    freq ={}
    for i in range(n):
        if arr[i] in freq:
            freq[arr[i]]+=1
        else:
            freq[arr[i]]=1
    print(freq)
    for num in freq:
        if freq[num]>1:
            print(num)
#duplicate

arr = [22,11,44,55,22,33,11,66,77,88,99,11,55]
n = len(arr)
print(duplicate(arr,n))
