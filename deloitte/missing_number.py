def missing_no(arr,n):
    total_sum = n*(n+1) //2
    actual_sum = sum(arr)
    # print(total_sum,actual_sum)
    return total_sum - actual_sum

arr = [1,2,3,5,6,7,8,9,10]
n = len(arr) + 1

print(missing_no(arr,n))