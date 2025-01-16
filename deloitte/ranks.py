N = int(input())
ranks = list(map(int, input().split()))
cuts = 0
prev_rank = ranks[0]
for rank in ranks[1:]:
    if rank < prev_rank: 
        cuts+= 1
    prev_rank = rank
print(cuts)