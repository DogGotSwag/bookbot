from stats import get_num_of_characters, sort_dict, num_of_words
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_of_word_in_book = num_of_words(text)
    char_dict = get_num_of_characters(text)
    sorted_dict = sort_dict(char_dict)

    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f"Found {num_of_word_in_book} total words")
    print('--------- Character Count -------')
    for key in sorted_dict:
        if key["char"].isalpha():
            print(f"{key["char"]}: {key["num"]}")
    print('============= END ===============')

main()
