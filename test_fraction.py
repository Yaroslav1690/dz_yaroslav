from app.fraction import Fraction


def test_reduce():
    d = Fraction(5, 10)
    d.reduce()
    assert d.num == 1
    assert d.den == 2 


def test___str__():
    k = Fraction(1, 17)
    assert str(k) == "1/17"


def test_sub():
    m = Fraction(1, 3)
    n = Fraction(1, 6)
    assert m - n == Fraction(1, 6)


def test_add():
    m = Fraction(1, 6)
    n = Fraction(2, 3)
    assert m + n == Fraction(5, 6)


def test_mul():
    a = Fraction(2, 7)
    b = Fraction(1, 3)
    assert a * b == Fraction(2, 21)


def test_truediv():
    a = Fraction(5, 11)
    b = Fraction(1, 2)
    assert a / b == Fraction(10, 11)