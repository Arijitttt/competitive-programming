arr = [3, 5, 1, 6, 8, 1]

def largest_smallest(arr):
    temp = []
    temp.append(max(arr))
    temp.append(min(arr))
    return ' '.join(map(str, temp))

print(largest_smallest(arr)) 