# Functions
def get_text(path):
    with open(path) as f:
        return f.read()
    
def get_total_words(text):
    total_words = text.split()
    return len(total_words)

def count_letters(text):
    letters_dict = {}
    for letter in text:
        if letter.isdigit() == False and letter.isalpha():
            lowered_letter = letter.lower()
            if lowered_letter not in letters_dict:
                letters_dict[lowered_letter] = 1
            else:
                letters_dict[lowered_letter] += 1

    return letters_dict

def sort_on(item):
    return item[1]