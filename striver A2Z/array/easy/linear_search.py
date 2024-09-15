def linear_search(arr, N,K):
    for i in range(N):
        if arr[i] == K:
            return 1
    return -1
arr = [1,2,3,4,6]
N = 5
K = 6
print(linear_search(arr, N, K))