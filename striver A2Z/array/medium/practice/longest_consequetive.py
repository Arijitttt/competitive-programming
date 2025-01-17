def longest_consequetive(nums):
    if not nums:
        return 0
    num_set = set(nums)
    long = 0
    for num in num_set:
        if num-1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num+1 in num_set:
                current_num +=1
                current_streak += 1
            long = max(long,current_streak)
    print(long)
longest_consequetive([100, 4, 200, 1, 3, 2])