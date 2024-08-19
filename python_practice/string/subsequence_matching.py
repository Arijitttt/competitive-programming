def subsequence_matching(real,subswquence):
    if subswquence in real:
        return 'subsequence exist'
    return "subsequence does't exist"

print(subsequence_matching(real='abcd',subswquence='bc'))