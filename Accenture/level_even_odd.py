def level_odd_even(arr):
    level = []
    for i in range(len(arr)):
        if arr[i]%2==0:
            level.append('even')
        else:
            level.append('odd')
    # for i in range(len(level)-1,-1,-1):
    #     if level[i] == 'odd':
    #         level.pop(i)
    return ' '.join(level).replace('odd','')
print(level_odd_even([2,5,6,7,10]))