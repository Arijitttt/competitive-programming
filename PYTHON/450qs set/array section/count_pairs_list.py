def count_pairs(arr):
    key = int(input('enter key value: '))
    arr.sort()  # Ensure the array is sorted
    left = 0
    right = len(arr)-1
    count = 0

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == key:
            count += 1
            left += 1
            right -= 1
        elif current_sum < key:
            left += 1
        else:
            right -= 1


    return count

arr = [1, 5, 7, 1]
print(count_pairs(arr))
