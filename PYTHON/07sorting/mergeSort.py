def mergeSort(arr):
    #<!--- check if array length is more than 1 --->
    if len(arr) > 1:
        #<!--- divide the array into two equal halves --->
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        #<!--- call mergeSort on the left and right halves --->
        mergeSort(left_arr)
        mergeSort(right_arr)

        #<!--- merge the two sorted halves --->
        i = 0 # left array index
        j = 0 # right array index
        k = 0 # merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        #<!--- copy any remaining elements --->
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

# test the function
arr_test = [2,3,5,1,7,4,4,4,2,6,8]
mergeSort(arr_test)
print(arr_test)
