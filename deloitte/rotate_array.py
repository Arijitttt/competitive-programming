def rotate_array(arr,k):
    n = len(arr)
    k = k%n
    rotated_array = arr[-k:]+arr[:-k]
    return rotated_array
print(rotate_array([1,2,3,4,5],2))