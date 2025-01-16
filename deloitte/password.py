def password(a,b):
    result = ''
    i,j = 0,0
    while i < len(a) and j < len(b):
        result += a[i] + b[j]
        i += 1
        j += 1
    while i < len(a):
        result += a[i]
        i += 1
    while j < len(b):
        result += b[j]
        j += 1
    return result
print(password('open','source'))