def num_of_words(text):
    words_array = text.split()
    return len(words_array)

def get_num_of_characters(text):
    dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in dict:
            dict[lowered] += 1
        else:
            dict[lowered] = 1

    return dict

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    new_dict = []
    for key in dict:
        new_dict.append({"char": key, "num": dict[key]})
    new_dict.sort(reverse=True, key=sort_on)
    return new_dict