from app.fraction import Fraction
import pytest


a = ([Fraction(1, 1), Fraction(1, 1)])
b = ([Fraction(-1, 1), Fraction(1, 1)])
c = ([Fraction(1, -1), Fraction(-1, 1)])
d = ([Fraction(-1, 1), Fraction(-1, 1)])
e = ([Fraction(-1, -1), Fraction(-1, -1)])
f = ([Fraction(1), Fraction(1, 2)])
g = ([Fraction(-1), Fraction(1, 2)])
h = ([Fraction(1), Fraction(-1, 2)])
k = ([Fraction(-1), Fraction(-1, -2)])

def test_reduce():
    d = Fraction(5, 10)
    d.reduce()
    assert d.num == 1
    assert d.den == 2 


def test_str():
    k = Fraction(1, 17)
    assert str(k) == "1/17"


@pytest.mark.parametrize(
    ('a', 'b', 'c'), [
        [*a, Fraction(0, 1)],
        [*b, Fraction(-2, 1)],
        [*c, Fraction(0, 1)],
        [*d, Fraction(0, 1)],
        [*e, Fraction(0, 1)],
        [*f, Fraction(1, 2)],
        [*g, Fraction(-3, 2)],
        [*h, Fraction(3, 2)],
        [*k, Fraction(-3, 2)]
    ])
def test_sub(a, b, c):
   assert a - b == c


@pytest.mark.parametrize(
    ('a', 'b', 'c'), [
        [*a, Fraction(2, 1)],
        [*b, Fraction(0, 1)],
        [*c, Fraction(-2, 1)],
        [*d, Fraction(-2, 1)],
        [*e, Fraction(2, 1)],
        [*f, Fraction(3, 2)],
        [*g, Fraction(-1, 2)],
        [*h, Fraction(1, 2)],
        [*k, Fraction(-1, 2)]
    ])
def test_add(a, b, c):
    assert a + b == c


@pytest.mark.parametrize(
    ('a', 'b', 'c'), [
        [*a, Fraction(1, 1)],
        [*b, Fraction(-1, 1)],
        [*c, Fraction(-1, -1)],
        [*d, Fraction(1, 1)],
        [*e, Fraction(1, 1)],
        [*f, Fraction(1, 2)],
        [*g, Fraction(-1, 2)],
        [*h, Fraction(-1, 2)],
        [*k, Fraction(-1, 2)]
    ])
def test_mul(a, b, c):
    assert a * b == c


@pytest.mark.parametrize(
    ('a', 'b', 'c'), [
        [*a, Fraction(1, 1)],
        [*b, Fraction(-1, 1)],
        [*c, Fraction(1, 1)],
        [*d, Fraction(-1, -1)],
        [*e, Fraction(1, 1)],
        [*f, Fraction(2, 1)],
        [*g, Fraction(-2, 1)],
        [*h, Fraction(-2, 1)],
        [*k, Fraction(-2, 1)]
    ])
def test_truediv(a, b, c):
    assert a / b == c


