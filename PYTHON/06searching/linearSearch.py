# a = [77,33,55,66,11,22,99]
# key=int(input('enter key value: '))
# f=False
# for i in range(len(a)):

#     if a[i] == key:
#         print('key found at index',i)
#         f=True
# if not f:
#     print('not founded')

def LinerSearch(myList,key):
    for i in range(len(myList)):
        if myList[i]==key:
            return i
    return -1
myList=[77,33,55,66,11,22,99]
key=int(input('enter key value: '))
extra = []
position = LinerSearch (myList,key)
if position != -1:
    print(position)
elif position == -1:
    myList.append(key)
    print(myList)
    LinerSearch(myList,key)
