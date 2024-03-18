
from tools import *

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
    
main()