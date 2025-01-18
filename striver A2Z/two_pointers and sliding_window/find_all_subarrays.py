def find_all_subarrays(arr):
    n = len(arr)
    subArrays = []
    for window_size in range(1,n+1):
        for start in range(n-window_size +1):
            end  =start +window_size
            #print(f"window ise = {window_size} start = {start} end={end}")
            subArray  = arr[start:end]
            subArrays.append(subArray)
    return subArrays

arr = "hello"
print(find_all_subarrays(arr))