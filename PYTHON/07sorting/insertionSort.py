#insertion Sort

sortingList = [66,11,33,44,99,77]

for i in range(1,len(sortingList)):
    key = sortingList[i]
    j = i-1
    while j>=0 and key<sortingList[j]:
        sortingList[j+1] = sortingList[j]
        j = j-1
    sortingList[j+1] = key

print("Sorted List: ", sortingList)