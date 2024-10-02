def find_floor(A,N,X):
    low = 0
    high = N-1
    ans = -1
    while low<=high:
        mid = (low+high)//2 
        if A[mid]==X:
            return mid
        elif A[mid]<=X:
            ans = mid
            low = mid + 1
        else:
            high = mid -1
    return ans

A = [1,2,8,10,11,12,19]
N = len(A)
X = 5
print(find_floor(A,N,X))