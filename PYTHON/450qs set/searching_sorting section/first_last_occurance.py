# def first_last_occurance(arr,n,x):
#     low  = 0
#     high = n-1
#     while low<= high:
#         mid = (low+high)//2
#         if arr[mid] == x:
#             if mid == 0 or arr[mid-1] != x:
#                 return mid
#             high = mid-1
#         elif arr[mid] < x:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1
# arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
# print(first_last_occurance(arr, len(arr), 125))  # Output: 3

# def first_last_occurance(arr,n,x):
#     a,b = 0,0
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i] == arr[j]:
#                 l = arr[i]
#                 r = arr[j]
#                 while l!=r:
#                     c = r
#                     print(c)
#                     r += 1
#             # if arr[i] == arr[j]:
#             #     a = i
#             #     if arr[i] != arr[j]:
#             #         b = j
#             # if arr[i] != arr[j]:
#             #     b = j
#             #return a,b

#             # while arr[i] == arr[j]:
#             #     print('')
#     return -1



# def first_last_occurance(arr,n,x):
#     first  = -1
#     last = -1
#     for i in range(n):
#         if arr[i]==x:
#             if first == -1:
#                 first = i
#             last = i
#     if first != -1 and last != -1:
#         return first,last
#     else:
#         return -1

#optimized approach
def first_last_occurance(arr,n,x):
    def find_first(arr,low,high,x):
        if high >= low:
            mid = (low+high)//2
            if (mid == 0 or x>arr[mid-1]) and arr[mid]==x:
                return mid
            elif x>arr[mid]:
                return find_first(arr,mid+1,high,x)
            else:
                return find_first(arr,low,mid-1,x)
        return -1

    def find_last(arr,low,high,x):
        if low<=high:
            mid = (low+high)//2
            if(mid == n-1 or x<arr[mid+1]) and x==arr[mid]:
                return mid
            elif x<arr[mid]:
                return find_last(arr,low,mid-1,x)
            else:
                return find_last(arr,mid+1,high,x)
        return -1
    first = find_first(arr,0,n-1,x)
    if first == -1:
        return -1
    last = find_last(arr,0,n-1,x)
    return first,last
arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
print(first_last_occurance(arr, len(arr), 5))


