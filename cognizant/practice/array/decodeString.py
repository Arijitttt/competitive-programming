def frequency(s):
    stack = []
    for char in s:
        if char != ']':
            stack.append(char)
        else:
            decode = ''
            while stack[-1] != '[':
                decode = stack.pop() + decode
            stack.pop()
            repeat = ''
            while stack and stack[-1].isdigit():
                repeat = stack.pop() + repeat