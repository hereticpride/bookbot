from stats import count_words
from stats import count_characters
from stats import sorted_list

def main():
    book = "./books/frankenstein.txt"
    get_book = get_book_text(book)
    num_words = count_words(get_book)
    num_chars = count_characters(get_book)
    sort_chars = sorted_list(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_dict in sort_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


main()
