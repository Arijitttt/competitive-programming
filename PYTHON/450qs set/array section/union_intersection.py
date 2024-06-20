x = {5,2,3,4,1,2,6,7,3}
y = {77,11,22,3,4,1,2,6,7}
sorted_x = sorted(x)
sorted_y = sorted(y)
#union
print("Union of x and y: ", sorted_x + sorted_y)

#intersection
print("Intersection of x and y: ", list(set(sorted_x) & set(sorted_y)))
#difference
print("Difference of x and y: ", list(set(sorted_x) - set(sorted_y)))
print("Difference of y and x: ", list(set(sorted_y) - set(sorted_x)))
#symmetric difference
print("Symmetric difference of x and y: ", list(set(sorted_x) ^ set(sorted_y)))
#cartesian product
cartesian_product = [(a,b) for a in sorted_x for b in sorted_y]
print("Cartesian product of x and y: ", cartesian_product)

