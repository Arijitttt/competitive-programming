def binarySearch(a, length):
    key = int(input("Enter the value you want to search: "))
    f = False
    low = 0
    high = length - 1

    while low <= high:
        mid = (low + high) // 2
        if a[mid] == key:
            print("key found at index", mid)
            f = True
            break
        elif a[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    if not f:
        print(key, 'not found in', a)
        a.append(key)
        a.sort()  # Ensure the list is sorted after appending
        length = len(a)  # Update the length of the list
        print('new list is:', a)
        binarySearch(a, length)

a = [33, 77, 44, 11, 88, 44, 33, 22, 88]
a.sort()  # Ensure the list is sorted before starting binary search
length = len(a)
print('list is:', a)
binarySearch(a, length)
