def max_product_subarray(arr):
    n = len(arr)
    if n == 0:
        return 0

    # Initialize the variables to the first element of the array
    max_ending_here = arr[0]
    min_ending_here = arr[0]
    max_so_far = arr[0]

    # Iterate through the array starting from the second element
    for i in range(1, n):
        num = arr[i]

        # When num is negative, max and min swap values
        if num < 0:
            max_ending_here, min_ending_here = min_ending_here, max_ending_here

        # Update max_ending_here and min_ending_here
        max_ending_here = max(num, max_ending_here * num)
        min_ending_here = min(num, min_ending_here * num)

        # Update the global max product found so far
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Example 1
arr1 = [6, -3, -10, 0, 2]
print(max_product_subarray(arr1))  # Output: 180

# Example 2
arr2 = [2, 3, 4, 5, -1, 0]
print(max_product_subarray(arr2))  # Output: 120
