def is_prime(num):
    for val in range(2, int(num ** (1/2)) + 1):
        if num%val == 0:
            return False
    return True

def prime(number):
    if number < 1:
        raise ValueError('Given number must be greater than one.')
    primes = []
    n = 2
    while len(primes) < number:
        if is_prime(n):
            primes.append(n)
        n += 1
    return primes[-1]
