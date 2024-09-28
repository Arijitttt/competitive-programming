def reverse_polish_notation(tokens):
    stack = []
    for token in tokens:
        if token == "+":
            stack.append(stack.pop()+stack.pop())
        elif token == "-":
            a= stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif token == "*":
            stack.append(stack.pop()*stack.pop())
        elif token == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(token))
    return stack

print(reverse_polish_notation(["2", "1", "+", "3", "*"]))