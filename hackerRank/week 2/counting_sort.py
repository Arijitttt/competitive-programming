def counting_sort(arr):
    # Step 1: Find the maximum value in the array to determine the range
    max_val = max(arr)

    # Step 2: Create a count array to store the count of each unique element
    count = [0] * (max_val + 1)

    # Step 3: Store the count of each element in the count array
    for num in arr:
        count[num] += 1

    # Step 4: Modify the count array to accumulate the counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 5: Build the output array
    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    # Step 6: Copy the output array back to the original array
    for i in range(len(arr)):
        arr[i] = output[i]

# Example usage
arr = [1, 1, 3, 2, 1]
counting_sort(arr)
print("Sorted array:", arr)
