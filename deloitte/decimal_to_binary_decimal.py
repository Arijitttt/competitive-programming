def decimal_to_binary_decimal(num):
    binary = bin(num)[2:]
    binary_str = list(binary)
    for i in range(len(binary_str)-1,-1,-1):
        if binary_str[i] == '1':
            binary_str[i] = '0'
        elif binary_str[i] == '0':
            binary_str[i] = '1'
    binary_l= ''.join( binary_str)
    decimal_val =int (binary_l,2)
    return decimal_val
print(decimal_to_binary_decimal(25))
