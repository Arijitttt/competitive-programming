def is_vowel(word):
    return word[0].lower() in 'aeiou'

def find_vowel_words_with_positions(words):
    # Create a list to store words and their positions
    vowels_with_positions = []

    for i in range(1, len(words) + 1):
        word = words[i - 1]
        if is_vowel(word):
            vowels_with_positions.append((i, word))
    
    # Print the words with their positions
    for position, word in vowels_with_positions:
        print(f"{position}:{word}")

# Example usage
sentence = "apple banana cherry orange mango"
words = sorted(sentence.split())
find_vowel_words_with_positions(words)
