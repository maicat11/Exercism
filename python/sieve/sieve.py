def sieve(limit):
    primes = [True] * (limit + 1)

    for p in range(2, limit + 1):
        if primes[p]:
            for n in range(p * 2, limit + 1, p):
                primes[n] = False

    return [i for i, m in enumerate(primes) if m][2:]
