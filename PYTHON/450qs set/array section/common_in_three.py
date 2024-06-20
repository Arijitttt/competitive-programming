first = [3,2,4,1,5,2,1]
second = [6,7,5,9,8,6,7,8]
third = [11,14,12,11,66,6,5]
# first.sort()
# second.sort()
# third.sort()
# print(first,second,third)
# for i in range(len(first)):
#     for j in range(len(second)):
#         for k in range(len(third)):
#             if first[i]==second[j]==third[k]:
#                 temp =  third[k]
#                 break
# print(temp)

#another way
set_first = set(first)
set_second = set(second)
set_third = set(third)

common_element = set_first.intersection(set_second,set_third)

print(common_element)