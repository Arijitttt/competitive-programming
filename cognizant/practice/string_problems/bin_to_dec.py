dec  = 9
bin_val = bin(dec)[2:].zfill(32)
bin_val = list(bin_val)
for c in range(len(bin_val)):
    if bin_val[c] == '1':
        bin_val[c] = '0'
    
    else:
        bin_val[c] = '1'
updated_bin_val = ''.join(bin_val)
print(int(updated_bin_val,2))