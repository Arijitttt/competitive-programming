def find_count(arr,length,num,diff):
    if not arr:
        return -1
    count = 0
    for value in range(length):
        if abs(arr[value]-num) <= diff:
            count += 1
    return count
if __name__=='__main__':
    arr = list(map(int,input().split()))
    length = len(arr)
    num = int(input())
    diff = int(input())
    print(find_count(arr,length,num,diff)) 