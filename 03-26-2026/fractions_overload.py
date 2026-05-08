import math


class Fraction:
    """Overloading Fraction class"""

    def __init__(self, num: int, denom: int):
        gcd = math.gcd(num, denom)
        self.num = num // gcd
        self.denom = denom // gcd

    def __str__(self):
        return f"{self.num}/{self.denom}"

    def __add__(self, other: "Fraction"):
        """Overloading addition"""
        numerator = self.num * other.denom + self.denom * other.num
        denominator = self.denom * other.denom

        return Fraction(numerator, denominator)

    def __sub__(self, other: "Fraction"):
        """Overloading subtraction"""
        numerator = self.num * other.denom - self.denom * other.num
        denominator = self.denom * other.denom

        return Fraction(numerator, denominator)

    def __mul__(self, other: "Fraction"):
        """Overloading multiplication"""
        return Fraction(self.num * other.num, self.denom * other.denom)

    def __truediv__(self, other: "Fraction"):
        """Overloading division. Errorguard for when other fraction has a 0 numerator"""
        if other.num == 0:
            raise ZeroDivisionError("You cannot divide by 0")

        return Fraction(self.num * other.denom, self.denom * other.num)


first = Fraction(1, 3)
second = Fraction(2, 4)
third = Fraction(0, 4)

print(first + second)
print(first - second)
print(first * second)
print(first / second)
print(first / third)
print(third / first)
