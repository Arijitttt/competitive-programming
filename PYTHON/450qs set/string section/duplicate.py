str = 'abaaacastreawcct'
dup = []
dup_count = {}

for i in range(len(str)):
    for j in range(i+1, len(str)):
        if str[i] == str[j] and str[i] not in dup:
            dup.append(str[i])
            if str[i] in dup_count:
                dup_count[str[i]] += 1
            else:
                dup_count[str[i]] = 2  # count the first occurrence as well

print("Duplicate characters:", dup)
print("Duplicate character counts:", dup_count)
