import math
from math import *


class Error:
    pass


class Fraction:

    def __init__(self, num: int = 0, den: int = 1) -> None:
        self.den = den
        self.num = num
    def inner(self) -> None:
        self.num = int(input('Введите числитель '))
        self.den = int(input('Введите знаменатель '))
        if self.den == 0:
            raise Error
    def __str__(self) -> str:
        return f"{self.num}/{self.den}"

    def __eq__(self, other: "Fraction") -> bool:
        return self.num == other.num and self.den == other.den

    def __add__(self, other):
        m = self.__lcm(self.den, other.den)
        n = self.num * (m // self.den) + other.num * (m // other.den)
        return Fraction(n, m)

    def __sub__(self, other):
        m = math.lcm(self.den, other.den)
        n = self.num * (m // self.den) - other.num * (m // other.den)
        return Fraction(n, m)

    def __mul__(self, other):
        m = self.num * other.num
        n = self.den * other.den
        return Fraction(m, n)

    def __truediv__(self, other):
        m = self.num * other.den
        n = self.den * other.num
        return Fraction(m, n)

    def reduce(self) -> None:
        if self.num == 0:
            return
        m = self.__gcd(self.den, self.num)
        self.den = self.den // m
        self.num = self.num // m


    def __lcm(self, a, b):
        return math.lcm(a, b)

    def __gcd(self, a, b):
        return math.gcd(a, b)


class IrreducibleFraction(Fraction):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reduce()


      
