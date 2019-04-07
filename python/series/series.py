from collections import deque


def slices(series, length):
    if series == '':
        raise ValueError('Series cannot be empty')
    if length <= 0:
        raise ValueError('Length must be greater than 0')
    if len(series) < length:
        raise ValueError('Series length must be greater than length')

    parts = []
    window = deque(maxlen=length)
    for val in series:
        window.append(val)
        if len(window) == length:
            parts.append(''.join(list(window)))
    return parts
