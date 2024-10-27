def count_negetive_growth_days(arr):
    count = 0
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            count += 1
    return count

if __name__ == "__main__":
    arr = list(map(int,input('input prices: ').split()))
    print(count_negetive_growth_days(arr))