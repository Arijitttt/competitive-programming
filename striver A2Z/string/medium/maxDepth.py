def maxDepth(s):
    a = [6,7]
    print(a.pop())
    stack = []
    max_depth = 0
    for c in s:
        if c == '(':
            stack.append(c)
            print(stack)
        elif c == ')':
            stack.pop()
            print(stack)

        max_depth = max(max_depth, len(stack))

    return max_depth
print(maxDepth("(1+(2*3)+((8)/4))+1"))
