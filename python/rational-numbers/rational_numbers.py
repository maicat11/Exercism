from __future__ import division
from math import gcd


class Rational(object):
    def __init__(self, numer, denom):
        if denom < 0:
            numer, denom = -numer, -denom
        self.numer = numer // gcd(numer, denom)
        self.denom = denom // gcd(numer, denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        add_numer = self.numer * other.denom + self.denom * other.numer
        add_denom = self.denom * other.denom
        if add_numer == 0:
            return Rational(add_numer, 1)
        return Rational(add_numer, add_denom)

    def __sub__(self, other):
        sub_numer = self.numer * other.denom - self.denom * other.numer
        sub_denom = self.denom * other.denom
        if sub_numer == 0:
            return Rational(sub_numer, 1)
        return Rational(sub_numer, sub_denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer**power, self.denom**power)

    def __rpow__(self, base):
        return (base**(1/self.denom))**self.numer