dec_value = 7
temp = []
while dec_value>0:
    temp.append(str(dec_value%2))
    
    dec_value = dec_value//2
output = ''.join(temp)
print(type(output))