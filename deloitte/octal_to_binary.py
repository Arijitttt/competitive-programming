def octal_to_binary(octal):
    return bin(int(octal,8))[2:]

octal = input()
print(octal_to_binary(octal))