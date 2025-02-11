def longest_substring_without_repeating_char(s):
    visited = set()
    left = 0
    max_len = 0
    for i in range(len(s)):
        while s[i] in visited:
            visited.remove(s[i])
            left += 1
        visited.add(s[i])
        max_len = max(max_len,i-left+1)
    return max_len
print(longest_substring_without_repeating_char('abcabcbb'))