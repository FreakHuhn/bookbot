from stats import count_words, count_letters, sort_count_letters
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        text = f.read()
    return text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")  
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    num_letters = count_letters(book_text)
    letter_list = sort_count_letters(num_letters)
    print(f"Found {num_words} total words.")
    for letter in letter_list:
        print(f"{letter['char']}: {letter['num']}")

main()
