arr =  [1,2,44,1,2,5,1,3,3,3,2,5]
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

sorted_freq = sorted(freq.items(),key=lambda x:(x[1],x[0]),reverse=True)

result = []

for num,frequency in sorted_freq:
    result.extend([num]*frequency)
print(' '.join(map(str,result)))
# sorted_list = list(freq.keys())

