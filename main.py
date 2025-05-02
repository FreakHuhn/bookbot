from stats import count_words, count_letters


def get_book_text(book_path):
    with open(book_path) as f:
        text = f.read()
    return text


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    num_letters = count_letters(book_text)
    print(f"{num_words} words found in the document.\n"
          f"Letter counts: {num_letters}")

main()
