def expand_compressed_string(s):
    result = []
    i = 0
    while i < len(s):
        char = s[i]
        i+=1
        count = 0
        while i<len(s) and s[i].isdigit():
            count = count*10 + int(s[i])
            i+=1
        result.append(char*count)
    return ''.join(result)
input_str = "a2b2c4"
output = expand_compressed_string(input_str)
print(output)  # Output: aabbcccc