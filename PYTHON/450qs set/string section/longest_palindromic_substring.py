#longest palindromic substring
def longest_palindromic_substring(str,n):
    res = ""
    resLen = 0
    for i in range(n):
        #odd length
        l,r = i,i
        while l>=0 and r<n and str[l]==str[r]:
            if (r-l+1)>resLen:
                res = str[l:r+1]
                resLen = r-l+1
            l-=1
            r+=1

        #even length
        l,r = i,i+1
        while l>=0 and r<n and str[l] == str[r]:
            if (r-l+1)>resLen:
                res = str[l:r+1]
                resLen = r-l+1
            l-=1
            r+=1
    print(res)
str = "aaaabbaa"
n = len(str)
longest_palindromic_substring(str,n)