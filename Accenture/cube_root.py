def cube_root(num):
    if num < 0:
        return False
    # for  i in range(1,num+1):
    #     if i**3 ==num:
    #         return i
    # return False

    for i in range(1,3):
        num = num//3
    return num
print(cube_root(27))