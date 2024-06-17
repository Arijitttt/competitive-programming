selection_srt = [33,11,66,22,33,99]
length = len(selection_srt)
for i in range(length):
    for j in range(i+1,length):
        if(selection_srt[i]>selection_srt[j]):
            selection_srt[i],selection_srt[j] = selection_srt[j],selection_srt[i]
print(selection_srt)