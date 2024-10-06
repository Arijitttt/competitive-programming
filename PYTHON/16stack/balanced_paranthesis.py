"""
Use a stack to check whether or not a string has balanced usage of paranthesis.

Example:
 (),()(),(({{[]}})) <- balanced
 ((),{{{)}],[][]]] <- not balanced

Balanced Example: {[]}

Non-balanced Example : (()

Non-balanced Example: }}s
"""

def is_parenthesis_balanced(paren_string):
    s = []
    is_balanced = True
    index = 0
    matching_paren = {')': '(', '}': '{', ']': '['}
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in '({[':
            s.append(paren)
        else:
            if s == []:
                is_balanced = False
            else:
                top = s.pop()
                if top != matching_paren[paren]:
                    is_balanced = False
        index += 1

    # Check if there are any remaining opening parentheses in the stack
    if s != []:
        is_balanced = False

    return is_balanced

print(is_parenthesis_balanced('({[]})'))  # True
print(is_parenthesis_balanced('(()'))  # False
print(is_parenthesis_balanced('}}s'))  # False

