def maxDepth(s):
    stack = []
    count,maxCount = 0,0
    for i in s:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        maxCount = max(count,maxCount)
    return maxCount
print(maxDepth("(1+(2*3)+((8)/4))+1"))