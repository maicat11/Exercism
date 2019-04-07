from string import ascii_lowercase

def is_pangram(sentence):
    sentence = sentence.lower()
    for char in ascii_lowercase:
        if char not in sentence:
            return False
    return True


