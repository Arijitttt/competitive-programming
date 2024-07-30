# Input : test_str = 'geeks5geeks', K = '7', i = 5 
# Output : 'geeks7geeks' 
# Explanation : Element is 5, converted to 7 on ith index.

test_str = 'geeks5geeks'
print('original String : ',str(test_str))

k = '4'

i = 5
for j in range(len(test_str)):
    if test_str[j] == '5':
        test_str = test_str.replace(test_str[j],k)
# test_str= test_str.replace(test_str[i],k,1)

print('the constructed string: ',test_str)