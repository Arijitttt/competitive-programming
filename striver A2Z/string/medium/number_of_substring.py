from collections import defaultdict

def countDist(s, k):
    # Helper function to count substrings with at most K distinct characters
    def atMostKDistinct(s, k):
        left = 0
        count = 0
        freq = defaultdict(int)
        
        for right in range(len(s)):
            # Add the current character to the frequency map
            freq[s[right]] += 1
            
            # Shrink the window if it has more than K distinct characters
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            
            # Add the number of valid substrings in the current window
            count += right - left + 1
        
        return count
    
    # Calculate the number of substrings with exactly K distinct characters
    return atMostKDistinct(s, k) - atMostKDistinct(s, k - 1)

s= 'abaaca'
k = 1
print(countDist(s,k))