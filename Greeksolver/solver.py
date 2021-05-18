"""
File: solver.py
-------------------
This program is a simple crossword solver for Attic Greek. The user inputs single letters
that might be part of a longer Greek word, such as when reading fragmentary texts,
and the program returns a list of possible matches
"""

LEXICON_FILE = "wordlist.csv"    # File to read word list from
import re

def get_fragment():
    fragment = input("Enter the fragment. There is no need to enter accents. For unknown letters use a full stop (.)  ")
    return fragment

def match_word(word, fragment):
    return re.fullmatch(fragment, word)

def get_words():
    fragment = get_fragment()
    file = open(LEXICON_FILE, "r", encoding="utf-8")
    words = file.readlines()
    list_of_words = []
    for word in words:
        word = word.strip('\n')
        if match_word(word, fragment):
            list_of_words.append(word)
    return list_of_words

def main():
    print(get_words())

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
