from string import digits


def verify(isbn):
    isbn = list(isbn.replace('-', '')[::-1])
    if not 9 < len(isbn) < 11:
        return False

    value = 0
    for i, num in enumerate(isbn):
        if i == 0 and num == 'X':
            value += 10
            continue
        if num not in digits:
            return False
        value += int(num) * (i+1)
    return value % 11 == 0
