arr = [1, 5, 8, 10]
k = int(input('enter the breakpoint: '))
print("Original array is:", arr)
print("Breakpoint is:", k)
diff = len(arr)-k
temp1 = []
temp2 = []
original_arr = []
length = len(arr)
for j in range(k-1):
    temp1.append(arr[j])
    temp1[j] = temp1[j]+k
for i in range(diff-1,length):
    temp2.append(arr[i]-k)
    # temp2[i]=temp2[i]-k
original_arr = temp1+temp2
print("Modified array is:", original_arr)
max = original_arr[0]
min = original_arr[0]
for i in range(len(original_arr)):
    if original_arr[i] > max:
        max= original_arr[i]
for i in range(len(original_arr)):
    if original_arr[i] < min:
        min = original_arr[i]
print('therefore difference between largest and lowest: ',max-min)