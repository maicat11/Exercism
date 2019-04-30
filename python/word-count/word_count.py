from string import punctuation
from collections import Counter

def word_count(phrase):
    phrase = phrase.replace('\t', ' ').replace('\n', ' ')
    check = punctuation.replace("'", '')

    for char in phrase:
        if char in check:
            phrase = phrase.replace(char, ' ')

    return Counter([x.lower().strip("'").strip('"') for x in phrase.split(' ') if x != ''])

