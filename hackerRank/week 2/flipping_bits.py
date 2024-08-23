def flipping_bits(n):
    #decimal to binary
    binary = bin(n)[2:]
    #make binary for 32 bit
    binary = binary.zfill(32)
    for digit in binary:
        if digit == '0':
            #make it 1 using replace
            binary = binary.replace(digit,'1',1)
        else:
            binary = binary.replace(digit,'0',1)
    flipped_binary = int(binary,2)
    return flipped_binary
print(flipping_bits(10))
