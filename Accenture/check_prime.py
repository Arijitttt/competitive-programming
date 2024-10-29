def check_prime(arr):
    count = 0
    for num in arr:
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                count += 1
    return count

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    print(check_prime(arr))
