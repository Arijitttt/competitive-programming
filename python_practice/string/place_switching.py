def place_switching(str1):

    # for i in range(len(str1)):
    #     if str1[i] == ' ':
    temp = str1.split()
    result = temp[1]+' '+temp[0]
    return result

print(place_switching('hello world'))