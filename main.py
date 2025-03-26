from stats import count_words, make_char_dict, character_count
from report import print_report
import sys

def get_book_text():
    if len(sys.argv) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
    book_path = sys.argv[1]
    with open(book_path) as book:
        return book.read()
        


def main():
    try:
        book_text = get_book_text()
    except Exception as e:
        print(e)
        sys.exit(1)
    word_count = count_words(book_text)
    character_dict = make_char_dict(book_text)
    char_count = character_count(character_dict)
    
    print_report(word_count,char_count,sys.argv[1])

main()    
    