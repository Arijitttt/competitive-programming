from itertools import permutations

def find_all_permutations(str):
    output = ''
    res = []
    value = permutations(str)

    for i in list(value):
        res.append(''.join(i))
    output = ' '.join(res)
    return output[:2]
print(find_all_permutations('ABC'))