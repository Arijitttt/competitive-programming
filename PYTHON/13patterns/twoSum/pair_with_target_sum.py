arr = [2, 5, 9, 11]
n = len(arr)
target = 11
# two sum method

left = 0
right = n-1

while left < right:
    if arr[left] + arr[right] == target:
        # print(arr[left],arr[right])
        print(f"index : {left},{right}")
        left+=1
        right-=1
    elif arr[left]+arr[right]<target:
        left+=1
    else:
        right-=1