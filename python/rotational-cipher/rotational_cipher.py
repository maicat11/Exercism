from string import ascii_lowercase

def rotate(text, key):
    encoded = []
    for char in text:
        if char.isalpha():
            i = (ascii_lowercase.index(char.lower()) + key) % 26
            if char.isupper():
                encoded.append(ascii_lowercase[i].upper())
            else:
                encoded.append(ascii_lowercase[i])
        else:
            encoded.append(char)
    return ''.join(encoded)
