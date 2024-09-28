double = lambda x: x*2
cube = lambda x:x*x*x
avg = lambda x,y:(x+y)/2
print(double(5))
print(cube(5))
print(int(avg(5,6)))

def appl(f, x):
    return f(x)
print(appl(lambda x: x*2, 5))
