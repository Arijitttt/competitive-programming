test_list = [3,5,6,8,10]
print('original list :  '+str(test_list))

max_ele = max(test_list)

# res = set(range(max_ele+1)).difference(set(test_list))\
res  = set(range(max_ele+1)).difference(set(test_list))

print('the list of missing elemenet : ',list(res))