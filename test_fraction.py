from app.fraction import Fraction
import pytest

def test_reduce():
    d = Fraction(5, 10)
    d.reduce()
    assert d.num == 1
    assert d.den == 2 


def test___str__():
    k = Fraction(1, 17)
    assert str(k) == "1/17"

a = ([Fraction(1, 1), Fraction(1, 1)])
b = ([Fraction(-1, 1), Fraction(1, 1)])
c = ([Fraction(1, -1), Fraction(-1, 1)])
d = ([Fraction(-1, 1), Fraction(-1, 1)])
e = ([Fraction(-1, -1), Fraction(-1, -1)])


@pytest.mark.parametrize(
    ('a', 'b', 'c'), [
        [*a, Fraction(0, 1)],
        [*b, Fraction(-2, 1)],
        [*c, Fraction(0, 1)],
        [*d, Fraction(0, 1)],
        [*e, Fraction(0, 1)]
    ] )


def test_sub(a, b, c):
   assert a - b == c


@pytest.mark.parametrize(
    ('a', 'b', 'c'), [
        [*a, Fraction(2, 1)],
        [*b, Fraction(0, 1)],
        [*c, Fraction(-2, 1)],
        [*d, Fraction(-2, 1)],
        [*e, Fraction(2, 1)]
    ] )


def test_add(a, b, c):
   assert a + b == c


@pytest.mark.parametrize(
    ('a', 'b', 'c'), [
        [*a, Fraction(1, 1)],
        [*b, Fraction(-1, 1)],
        [*c, Fraction(-1, -1)],
        [*d, Fraction(1, 1)],
        [*e, Fraction(1, 1)]
    ] )


def test_mul(a, b, c):
    assert a * b == c


@pytest.mark.parametrize(
    ('a', 'b', 'c'), [
        [*a, Fraction(1, 1)],
        [*b, Fraction(-1, 1)],
        [*c, Fraction(1, 1)],
        [*d, Fraction(-1, -1)],
        [*e, Fraction(1, 1)]
    ] )


def test_truediv(a, b, c):
    assert a / b == c