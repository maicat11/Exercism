from string import ascii_lowercase
reversed_ascii = ascii_lowercase[::-1]

def encode(plain_text):
    plain_text = plain_text.replace(',', '').replace('.', '').replace(' ', '').lower()

    encoded_vals = []
    for char in plain_text:
        if char.isalpha():
            encoded_vals.append(reversed_ascii[ascii_lowercase.index(char)])
        elif char.isdigit():
            encoded_vals.append(char)
    with_space = [el for y in [[el, ' '] if idx % 5 == 4 else el for idx, el in enumerate(encoded_vals)] for el in y]

    return ''.join(with_space).strip()


def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(' ', '')
    decoded_vals = [ascii_lowercase[reversed_ascii.index(x)] if x.isalpha() else x for x in ciphered_text]
    return ''.join(decoded_vals)
