def find_peak_elevation(arr):
    # low = 0
    # high = len(arr) - 1
    # while low < high:
    #     mid = (low + high) // 2
    #     if arr[mid] < arr[mid + 1]:
    #         low = mid + 1
    #     else:
    #         high = mid
    # return low
    
    low = 0
    high = len(arr)-1
    
    while low<high:
        mid = (low+high)//2
        if arr[mid]<arr[mid+1]:
            low = mid+1
        else:
            high = mid
    return arr[low]
    
    # return max(arr)


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(find_peak_elevation(arr))