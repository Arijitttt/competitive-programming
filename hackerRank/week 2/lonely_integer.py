def lonely_integer(a):
    for num in a:
        if a.count(num) == 1:
            return num

a  = [1,2,3,4,3,2,1]
print(lonely_integer(a))