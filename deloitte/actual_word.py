actual_word = 'HELLO'
rahul_word = 'EHLLO'
#print(sorted(actual_word.lower()))
# a = [1,2,3,4]
# b = [1,2,3,4]
# if a==b:
#     print('yes')

def anagram(actual_word,rahul_word):
    if len(actual_word) != len(rahul_word):
        return 0
    actual_word = sorted(actual_word.lower())
    rahul_word = sorted(rahul_word.lower())
    if actual_word !=rahul_word:
        return 0
    return 1
print(anagram(actual_word,rahul_word))