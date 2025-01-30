def duplicate(arr):
    n = len(arr)
    freq = {}
    for i in range(n):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1
    
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    for num,count in sorted_freq:
        print(f"{num} : {count}")
    

# Test with integers
#duplicate([1, 5, 6, 2, 1, 3, 1, 5, 6, 7, 1, 3, 2, 5, 6])

# Test with strings
#duplicate(['banana','apple', 'apple', 'orange', 'banana', 'apple'])

string = 'banana apple apple orange banana apple'
words = string.split()

duplicate(words)

