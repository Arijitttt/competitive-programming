def mars_exploration(s):
    c = 0
    expected = 'SOS' * (len(s)//3)
    for i in range(len(s)):
        if s[i] != expected[i]:
            c+=1
    return c
s = 'SOSSPSSQSSOR'
print(mars_exploration(s))