Mat=[[10,20,30,40],
[15,25,35,45],
[27,29,37,48],
[32,33,39,50]]
print(Mat)
print()
rows = len(Mat)
colums = len(Mat[0])
for i in range(rows):
    for j in range(colums):
        print(Mat[j][i],end=' ')
