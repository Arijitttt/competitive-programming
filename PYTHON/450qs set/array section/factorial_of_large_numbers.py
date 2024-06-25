def factorial(n):
    # Initialize the result list to store digits of factorial
    result = []

    # Calculate factorial of n
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    # Convert factorial into digits and add them to result list
    while fact > 0:
        digit = fact % 10
        result.insert(0, digit)  # Insert digit at the beginning of the list
        fact //= 10

    return result

# Example usage:
n = 6
print(factorial(n))
