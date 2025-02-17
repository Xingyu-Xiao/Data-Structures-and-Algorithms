from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_denominator = self.denominator * other.denominator
        new_numerator = self.numerator * other.denominator + (self.denominator * other.numerator)
        if gcd(new_denominator, new_numerator) == 1:
            return Fraction(new_numerator, new_denominator)
        else:
            g = gcd(new_denominator, new_numerator)
            return Fraction(new_numerator//g, new_denominator//g)


s = list(map(int, input().split()))
a = Fraction(s[0], s[1])
b = Fraction(s[2], s[3])
c = a + b
print(f'{c.numerator}/{c.denominator}')
