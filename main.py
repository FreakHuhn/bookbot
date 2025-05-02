def get_book_text(book_path):
    with open(book_path) as f:
        text = f.read()
    return text

def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")

main()
