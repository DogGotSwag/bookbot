from stats import num_of_words

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    text = get_book_text('./books/frankenstein.txt')
    num_of_word_in_book = num_of_words(text)
    print(f"{num_of_word_in_book} words found in the document")

main()