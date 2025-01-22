def anagram(word1,word2):
    if len(word1) != len(word2):
        return False
    if sorted(word1.lower()) == sorted(word2.lower()):
        return True
    return False
print(anagram("anagram","nagaram")) 