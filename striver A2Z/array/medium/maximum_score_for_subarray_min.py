import sys
def maximum_score_for_subarray_min(arr):
    maxi = -sys.maxsize-1
    for i in range(len(arr)-1):
        sum =arr[i] + arr[i+1]
        maxi = max(maxi,sum)
    return maxi
print(maximum_score_for_subarray_min([4,3,1,5,6]))