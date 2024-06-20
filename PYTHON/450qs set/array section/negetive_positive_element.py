def storing_pos_neg(arr):
    positive = []
    negetive = []
    for i in range(len(arr)):
        if arr[i]<0:
            negetive.append(arr[i])
        elif arr[i]==0:
            arr.remove(0)
        else:
            positive.append(arr[i])
    print('actual list: ',arr)
    print('after separating....')
    print('positive list: ',positive)
    print('negetive list: ',negetive)
arr = [-9,4,8,9,-1,4,-3,1,4,-33,0]
arr1 = []
for i in range(5):
    val = (int(input("Enter the number: ")))
    if val==0 or val==1 or val==2:
        arr1.append(val)
    else:
        print("won't accept")
print(arr1)
storing_pos_neg(arr)