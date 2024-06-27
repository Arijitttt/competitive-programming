def duplicate(str,n):
    freq = {}

    for i in range(n):
        if str[i] in freq:
            freq[str[i]] += 1
        else:
            freq[str[i]]=1
    # print(freq)
    # print()
    for num in freq:
        if freq[num]>1:
            #print(num,':',freq[num])
            print(f'{num},count : {freq[num]}')


str = 'geeksforgeeks'
n = len(str)
print(duplicate(str,n))