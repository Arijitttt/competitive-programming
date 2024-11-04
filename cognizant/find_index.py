def findIndex(arr,k):
    #arr.sort()
    # low = 0
    # high = len(arr)-1
    # while low <= high:
    #     mid = (low+high)//2
    #     if arr[mid] == k:
    #         return mid
    #     elif arr[mid]>k:
    #         high = mid-1
    #     else:
    #         low = mid+1
    # return -1

    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1

print(findIndex([5, 4, 6, 1, 3, 2, 7, 8, 9],7))