def isomorphic_string(s,t):
    if len(s) != len(t):
        return False
    else:
        map1,map2 = {},{}
        for i in  range(len(s)):
            ch1,ch2 = s[i],t[i]
            if ch1 not in map1:
                map1[ch1]  = ch2
            if ch2 not in map2:
                map2[ch2] = ch1
            print(map1,map2)
            if map1[ch1] != ch2 or map2[ch2] != ch1:
                return False
    return True 
print(isomorphic_string("egg","add"))