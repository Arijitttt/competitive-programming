def decimal_spikes(num,spike):
    binary = bin(num)[2:]
    after_spiking = binary[:-spike] if spike < len(binary) else '0'
    decimal = int(after_spiking,2)
    return decimal
def checking(arr,spike):
    b = []
    for  i in range(len(arr)):
        b.append(decimal_spikes(arr[i],spike))
    return b
arr = [4,5,0,1,9,0,5,0]
print(checking(arr,3))