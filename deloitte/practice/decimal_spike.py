def decimal_spike(num,spike):
    binary_1st = bin(num)[2:]
    after_spiking = binary_1st[:-spike] if spike<len(binary_1st) else '0'
    decimal = int(after_spiking,2)
    return decimal
def checking(arr,spike):
    n = len(arr)
    b = []
    for i in range(n):
        b.append(decimal_spike(arr[i],spike))
    return b
arr = list(map(int,input().split()))
spike = int(input())
print(checking(arr,spike))