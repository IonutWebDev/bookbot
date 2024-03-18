
def main():
    print("--- Begin report of books/frankenstein.txt ---")

    # Variables
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    total_words = get_total_words(text)
    total_letters = count_letters(text)


    # Print the total words
    print(f"{total_words} words found in the document\n")

    # Sort the dictionary reversly by its values
    sorted_letters_by_value = sorted(total_letters.items(), key=sort_on, reverse=True)

    # Print the total occurences of each letter
    for letter, occurrences in sorted_letters_by_value:
        print(f"The {letter} character was found {occurrences} times")


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
    
main()