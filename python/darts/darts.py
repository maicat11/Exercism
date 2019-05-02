from math import sqrt


def score(x, y):
    z = sqrt(x**2 + y**2)
    if z <= 1:
        return 10
    if z <= 5:
        return 5
    if z <= 10:
        return 1
    return 0