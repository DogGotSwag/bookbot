def num_of_words(text):
    words_array = text.split()
    return len(words_array)

def get_num_of_characters(text):
    dict = {}

    symbols_and_characters = list(text)
    for char in symbols_and_characters:
        lower_char = char.lower()
        if lower_char in dict:
            dict[lower_char] = dict[lower_char] + 1
        else:
            dict[lower_char] = 1

    return dict

