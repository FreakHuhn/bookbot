from stats import count_words, count_letters, sort_count_letters


def get_book_text(book_path):
    with open(book_path) as f:
        text = f.read()
    return text


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    num_letters = count_letters(book_text)
    letter_list = sort_count_letters(num_letters)
    print(f"Found {num_words} total words.")
    for letter in letter_list:
        print(f"{letter['char']}: {letter['num']}")

main()
