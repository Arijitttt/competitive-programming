def middle_of_three(A,B,C):

            # Determine the middle value
    if (A > B):
        if (A < C):
            return A
        elif (B > C):
            return B
        else:
            return C
    else:
        if (A > C):
            return A
        elif (B < C):
            return B
        else:
            return C

a = 918
b = 518
c = 300 
print(middle_of_three(a,b,c))