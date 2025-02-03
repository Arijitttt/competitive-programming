def longest_substring_without_repeating_charecters(s):
    n = len(s)
    start = 0
    max_len = 0
    visited = set()
    for end in range(n):
        while s[end] in visited:
            visited.remove(s[end])
            start += 1
        visited.add(s[end])
        max_len = max(max_len,end-start+1)
    return max_len
print(longest_substring_without_repeating_charecters("abcabcbb"))