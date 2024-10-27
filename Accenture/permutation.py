from itertools import permutations

def all_permutations(str):
    # permList = permutations(str)
    # print(type(permList))
    # for perm in list(permList):
    #     print(''.join(perm))
    output = ''
    twmp = []
    premList = permutations(str)

    for perm in list(premList):
        # output = output+''.join(perm).strip()
        twmp.append(''.join(perm).strip())

    output = ' '.join(twmp)
    print(output)
    # output = ' '.join(twmp)
    # return output
if __name__ == "__main__":
    str = 'ABC'
    print(all_permutations(str))