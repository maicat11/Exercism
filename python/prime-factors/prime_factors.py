def factors(value):
    prime_factors = []
    test_val = 2
    while value > 1:
        if value % test_val:
            test_val += 1
        else:
            prime_factors += [test_val]
            value /= test_val
    return prime_factors