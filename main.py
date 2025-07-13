def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def num_of_words(text):
    words_array = text.split()
    return len(words_array)

def main():
    text = get_book_text('./books/frankenstein.txt')
    num_of_word_in_book = num_of_words(text)
    print(num_of_word_in_book)

main()