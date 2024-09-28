def my_atoi(s):
    s = s.strip()
    if s[0] in 'abcdefghijklmnopqrstuvwxyz':
        return 0
    has_non_numeric =False
    length = len(s)
    i = 0
    while i < length:
        
        if s[i] not in '0123456789':
            return s[:i]
        if s[i] == '0':
            s =s.replace('0', '')
            length -= 1
        if s[i] in 'abcdefghijklmnopqrstuvwxyz':
            has_non_numeric  =True
            return s[:i]
        
        i += 1
    if has_non_numeric:
        return 0
    
    return s
print(my_atoi("  0-1"))