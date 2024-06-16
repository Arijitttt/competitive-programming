#make a list with all datatypes
my_list = [1, "hello", 3.14, True, 1,2 ]
# print(type(my_list[3]))
# print(my_list[-1])
# print(my_list[1:-3])
#list slicing
#print(my_list[1:3])
print(my_list[::-1])
#list indexing
print(my_list[0])
#list methods
my_list.append("new item")
print(my_list)
#insert method
my_list.insert(2,"inserted item")
print(my_list)
#extend method

my_list.extend([1,2,3])

print(my_list)
#remove method
my_list.remove("hello")
print(my_list)
#pop method
print(my_list.pop(0))
print(my_list)
#sort method
sorted = [66,33,11,33,44,11,22,99,55,66]
sorted.sort()
print(sorted)
#reverse method
my_list.reverse()
print(my_list)
#count method
print(my_list.count(1))
#clear method
my_list.clear()
print(my_list)
#copy method
c_list = [1,2,3,4,5]
c_list_copy = c_list.copy()
print(c_list_copy)
#list comprehension
new_list = [x**2 for x in range(1,6)]
print(new_list)
#enumerate
for i, value in enumerate(new_list):
    print(f"index: {i}, value: {value}")

