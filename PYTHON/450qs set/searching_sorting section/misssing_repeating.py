def findTwoElement(arr, n):
    # Initialize variables for the repeating and missing numbers
    missing = -1
    reapeating = -1

    freq =[0]*(n+1)

    for num in arr:
        freq[num] += 1

    for i in range(1,n+1):
        if freq[i] == 0:
            missing = i
        elif freq[i] > 1:
            reapeating = i
    return [reapeating,missing]

# Test cases
random_list = [2, 2]
print(findTwoElement(random_list, 2))  # Output: [2, 1]

random_list = [1, 3, 3]
print(findTwoElement(random_list, 3))  # Output: [3, 2]
