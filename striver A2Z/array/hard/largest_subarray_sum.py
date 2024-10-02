def largest_subarray_with_zero_sum(n,arr):
    sum = 0
    maxi = 0
    mpp = {}
    for num in range(n):
        sum  = sum+arr[num]
        if sum == 0:
            maxi = num+1
        else:
            if sum in mpp:
                maxi = max(maxi,num-mpp[sum])
            else:
                mpp[sum] = num
    return maxi

print(largest_subarray_with_zero_sum(8,[15,-2,2,-8,1,7,10,23]))