

def print_report(word_count,char_count,book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in char_count:
        print(f"{i}: {char_count[i]}")
    print("============= END ===============")
