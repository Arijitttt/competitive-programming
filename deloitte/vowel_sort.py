# def is_vowel(c):
#     return c in 'aeiouAEIOU'
# input_str = "apple banana cherry orange mango"
# words = input_str.split()
# words.sort()
# for i, word in enumerate(words, 1):
#     if is_vowel(word[0]):
#         print(f"{i}: {word}")
def is_vowel(c):
    return c in 'aeiouAEIOU'
string = input()
words = string.split()
words.sort()
for i,word in enumerate(words,1):
    if is_vowel(word[0]):
        print(f"{i}:{word}")