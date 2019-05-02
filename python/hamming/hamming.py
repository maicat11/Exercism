def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be the same length.')

    counter = 0
    for i, s in enumerate(strand_a):
        if strand_b[i] != s:
            counter += 1
    return counter