def substring_with_0_1(str,n):
    count_0 = 0
    count_1 = 0

    cnt = 0

    for i in range(n):
        if str[i] == '0':
            count_0 += 1
        if str[i] == '1':
            count_1 += 1

        if count_0 == count_1:
            cnt += 1

    if count_0 != count_1 :
        return -1
    return cnt


str ='0111100010'
print(substring_with_0_1(str,len(str)))