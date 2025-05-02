def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_letters(text):
    letters = {}
    for char in text.lower():
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters
