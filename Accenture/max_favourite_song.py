def max_favourite_song(s,k):
    max_count = 0
    current_count = 0
    for i in range(k):
        if s[i] == 'a':
            current_count += 1
    max_count = current_count