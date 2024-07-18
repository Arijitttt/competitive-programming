def rotation_string(S1,S2):
    # if len(S1) and len(S2) != 4:
    #     return 0
    pivot = len(S1)//2
    temp1 = ""
    temp2 = ""
    for i in range(pivot):
        temp1 += S1[i]
    for j in range(pivot,len(S1)):
        temp2 += S1[j]
    if temp2+temp1 == S2:
        print("strings are rotating")
S1 = "ABCD"
S2 = "CDAB"
rotation_string(S1,S2)