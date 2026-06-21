import sys

from stats import chars_dict_to_sorted_list, get_chars_dict, get_num_words


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)

    # Convert chars_dict to a sorted list of tuples
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"=========== BOOKBOOT =============")
    print(f"Analyzing book found at {book_path}...")
    print(f"---------- Word Count ------------")
    print(f"Found {num_words} total words")
    print(f"------- Character Count ----------")
    for item in chars_sorted_list:
        char, count = item

        # Skip non-alphabetic chars
        if char.isalpha():
            print(f"('{char}', {count})")

    print(f"============= END ===============")


def get_book_text(path):
    # TODO: Validate path
    with open(path) as f:
        return f.read()


main()
