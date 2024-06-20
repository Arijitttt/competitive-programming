def rotation(arr,length,pivot):
    j=0
    temp = []
    while(j<pivot):
        temp.append(arr[j])
        j=j+1
    j=0
    while(pivot<length):
        arr[j]=arr[pivot]
        j=j+1
        pivot = pivot+1
    arr[:]=arr[:j]+temp
    return arr
arr = [2,1,3,5,6,3]
length = len(arr)
low = 0
high = length
pivot  = (low+high)//2
print(rotation(arr,length,pivot))