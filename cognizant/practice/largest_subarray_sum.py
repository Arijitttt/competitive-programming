def largest_sum(arr):
    current_max = arr[0]
    max_soFar = arr[0]
    for num in arr[1:]:
        current_max = max(current_max+num,num)
        max_soFar = max(current_max,max_soFar)
    return max_soFar
print(largest_sum([-2,1,-3,4,-1,2,1,-5,4]))