def largest_element(arr):
    return max(arr)

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    print(largest_element(arr))