def longest_substring_without_repeating_charecters(s):
    visited = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in visited:
            visited.remove(s[right])
            left += 1
        visited.add(s[right])
        max_len = max(max_len,right-left+1)
    return max_len
print(longest_substring_without_repeating_charecters('abcabcbb'))