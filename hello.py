from itertools import chain
import re
__pragma__ ('alias', 'S', '$')

LEXICON_FILE = "wordlist.csv"    # File to read word list from

def get_fragment():
    # fragment = input("Enter the fragment. There is no need to enter accents. For unknown letters use a full stop (.)  ")
    #fragment = "ἀβεβα.*"
    fragment = document.getElementById("fragment").value
    return fragment

def match_word(word, fragment):
    return re.fullmatch(fragment, word)

def success(result):
    document.getElementById('idPlace').innerHTML = "Got words, searching..."
    words = get_words(result)
    combined = "<p>Results:</p>"
    for w in words:
        combined = combined + "<p>{}</p>".format(w)
    document.getElementById('idPlace').innerHTML = combined

def fail(a,b,c):
    document.getElementById('idPlace').innerHTML = "failed!"

def load_wordlist():
    S.ajax({
        'url':'wordlist.csv',
        'type':'GET',
        'datatype':'text',
        'success':success,
        'fail':fail
    })


def get_words(wordlist):
    words = wordlist.split("\n")
    fragment = get_fragment()
    list_of_words = []
    for word in words:
        word = word.strip('\n')
        if match_word(word, fragment):
            list_of_words.append(word)
    return list_of_words


def Thing():
    response = get_words()
    document.getElementById('idPlace').innerHTML = response

def DoThing():
    document.getElementById('idPlace').innerHTML = "working..."
    load_wordlist()
    