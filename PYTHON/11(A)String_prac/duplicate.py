def duplicate(str):
    #duplicate

    freq ={}
    n = len(str)
    for i in range (n):
        if str[i] in freq:
            freq[str[i]]+=1 
        else:
            freq[str[i]] = 1
    for num in freq:
        if freq[num] > 1:
            print(f'{num},count : {freq[num]}')
str = "geekforgeeks"
print(duplicate(str))