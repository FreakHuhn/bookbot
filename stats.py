def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_letters(text):
    letters = {}
    for char in text.lower():
        if char.isalpha() and char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def sort_count_letters(letters):
    #dictionary in einzele dictonarys umwandeln
    letter_list = []
    for char, num in letters.items():
        if  char.isalpha():
            letter_list.append({"char":char,"num":num})
    #sortieren
    letter_list.sort(reverse=True, key=lambda x: x["num"])
    return letter_list
       