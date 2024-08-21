def breaking_the_records(scores):
    min_count,max_count  = 0,0
    min_record = max_record = scores[0]

    for value in scores[1:]:
        if value > max_record:
            max_count += 1
            max_record = value
        elif value < min_record:
            min_count += 1
            min_record = value
    return [max_count,min_count]

scores = [12,24,10,24]
print(breaking_the_records(scores))
