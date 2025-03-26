from stats import get_num_words, get_num_letters, sort_characters
import sys

def get_book_text (path_to_file):
    with open(path_to_file) as file:
        return file.read()

def print_output(book, num_words, sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i, val in sorted:
        if i.isalpha():
            print(f"{i}: {val}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text('./' + book)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    sorted = sort_characters(num_letters)
    print_output(book, num_words, sorted)
main()
