def majority_element(A,N):
    temp = {}
    for num in A:
        if num in temp:
            temp[num]+=1
        else:
            temp[num] = 1
    for i in temp:
        if temp[i]> N//2:
            return i
        return -1
A = [3,1,3,3,2]
N = len(A)
print(majority_element(A,N))

