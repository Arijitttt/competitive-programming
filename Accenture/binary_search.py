def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    while low <=high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            high = mid-1
        else:
            low = mid+1
    return -1
if __name__ == "__main__":
    # arr = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr.sort()
    target = int(input())
    print(binary_search(arr,target))