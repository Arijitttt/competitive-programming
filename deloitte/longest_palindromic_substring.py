def longest_palindromic_substring(s):
    n = len(s)
    start,end = 0,0
    if n ==0:
        return ''
    def expand(left,right):
        while left>=0 and right<n and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1,right-1
    for i in range(n):
        l1,r1 = expand(i,i)
        l2,r2 = expand(i,i+1)

        if r1-l1 > end-start:
            start = l1
            end = r1
        if r2-l2 > end-start:
            start = l2
            end = r2
    return s[start:end+1]

print(longest_palindromic_substring("babad"))