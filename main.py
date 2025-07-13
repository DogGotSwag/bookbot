from stats import num_of_words
from stats import get_num_of_characters, sort_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    text = get_book_text('./books/frankenstein.txt')
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