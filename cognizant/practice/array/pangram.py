def pangram(s):
    letters = set()
    s = s.lower()
    for char in s:
        if 97 <= ord(char) <= 122 :
            letters.add(char)
    return len(letters) ==  26 
    
print(pangram('We promptly judged antique ivory buckles for the next prizeeeeee'))