from stats import count_words, make_char_dict, character_count
from report import print_report

def get_book_text(book_path):
    with open(book_path) as book:
        return book.read()


def main():
    book_path = "./books/frankenstein.txt"
    frankenstein_text = get_book_text(book_path)
    word_count = count_words(frankenstein_text)
    character_dict = make_char_dict(frankenstein_text)
    char_count = character_count(character_dict)
    
    print_report(word_count,char_count,book_path)


main()    
    