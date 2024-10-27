def find_equilibrium_index(arr):
    """
    Finds the index of an equilibrium point in the array, where the sum of elements
    on the left of the index is equal to the sum of elements on the right of the index.

    Parameters:
    arr (list of int): An integer array of size n.

    Returns:
    int: The index of an equilibrium point, or -1 if no equilibrium point exists.
    """
    total_sum = sum(arr)
    left_sum = 0

    for i, value in enumerate(arr):
        # Calculate the right sum by subtracting the left sum and the current element from total
        right_sum = total_sum - left_sum - value
        
        # Check if left and right sums are equal
        if left_sum == right_sum:
            return i
        
        # Update the left sum for the next position
        left_sum += value

    return -1

arr = [3, 1, 5, 2, 3]
print(find_equilibrium_index(arr))