"""
File: solver.py
-------------------
This program is a simple crossword solver for Attic Greek. The user inputs single letters
that might be part of a longer Greek word, such as when reading fragmentary texts,
and the program returns a list of possible matches
"""

LEXICON_FILE = "VoigtSappho"    # File to read word list from

def process():
    with open(LEXICON_FILE, "r", encoding="utf-8") as inputFile:
        lines = inputFile.readlines()
        output = []

        ### sinead things here
        # for line in lines:
        #     output.append(line)

        return output

def main():
    output = process()
    with open('processed.txt', "w", encoding="utf-8") as outputFile:
        outputFile.writelines(output)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
