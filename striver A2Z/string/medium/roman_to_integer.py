def roman_to_integer(s):
    value,i = 0,0
    length = len(s)
    while i < length:
        if i+1 < length and s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
            value -= 1

        elif i+1 < length and s[i] =='X' and (s[i+1] =='L' or s[i+1] == 'C'):
            value -= 10
        
        elif i+1 < length and s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == "M"):
            value -= 100
        
        else:
            if s[i] == 'M':
                value += 1000
            elif s[i] == 'D':
                value += 500
            elif s[i] == 'C':
                value += 100
            elif s[i] == 'L':
                value += 50
            elif s[i] == 'X':
                value += 10
            elif s[i] == 'V':
                value += 5
            elif s[i] == 'I':
                value += 1
        i += 1
    return value

        
print(roman_to_integer('MCMXCIV'))