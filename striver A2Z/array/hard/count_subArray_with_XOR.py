def countSubarraysWithXor(A, B):
    prefix_xor = 0  # Initial prefix XOR
    count = 0       # Count of subarrays with XOR equal to B
    freq = {}       # Dictionary to store the frequency of prefix XORs
    
    for num in A:
        # Update the current prefix XOR
        prefix_xor ^= num
        
        # If the prefix XOR itself is equal to B, increment the count
        if prefix_xor == B:
            count += 1
        
        # Calculate the required XOR value that would lead to XOR B
        required_xor = prefix_xor ^ B
        
        # If required_xor exists in freq, add its frequency to count
        if required_xor in freq:
            count += freq[required_xor]
        
        # Add the current prefix_xor to freq dictionary
        if prefix_xor in freq:
            freq[prefix_xor] += 1
        else:
            freq[prefix_xor] = 1
    
    return count

# Example usage
print(countSubarraysWithXor([4, 2, 2, 6, 4], 6))  # Output: 4
print(countSubarraysWithXor([5, 6, 7, 8, 9], 5))  # Output: 2
