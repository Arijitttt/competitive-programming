odd_even = [4,6,1,3,7,4,9]
even_sum,odd_sum = 0,0
for i in range(len(odd_even)):
    if odd_even[i]%2 == 0:
        even_sum += odd_even[i]
    else:
        odd_sum += odd_even[i]
print(even_sum,odd_sum)
