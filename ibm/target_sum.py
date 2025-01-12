def target_sm(arr,d):
    c= 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if (arr[i] + arr[j] + arr[k]) % d == 0:
                    c += 1
    return c
arr = [3,3,4,7,8]
print(target_sm(arr,5))
