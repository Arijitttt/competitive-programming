def flipping_bits(n):
    #decimal to binary
    binary = bin(n)[2:]
    #make binary for 32 bit
    binary = binary.zfill(32)
    #flip the bits
    flipped_binary = ''.join(
        '1' if bit == '0' else '0' for bit in binary
    )
    return int(flipped_binary, 2)
print(flipping_bits(10))
