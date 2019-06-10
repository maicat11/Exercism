def decode(string):
    digits = []
    decoded_string = []
    for char in string:
        if char.isdigit():
            digits.append(char)
        else:
            if len(digits) > 0:
                decoded_string.append(int(''.join(digits))*char)
                digits = []
            else:
                decoded_string.append(char)
    return ''.join(decoded_string)


def encode(string):
    encoded_list = []
    current_count = 0
    for i, char in enumerate(string):
        current_count += 1
        if (i == len(string) - 1) or (string[i+1] != char):
            encoded_list.append(str(current_count))
            encoded_list.append(char)
            current_count = 0
    return ''.join([x for x in encoded_list if x != '1'])
