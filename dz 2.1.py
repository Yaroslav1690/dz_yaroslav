class Fraction:
    def __init__(self, top=0, bottom=1):
        self.num = top
        self.den = bottom 
    
    def input(self):
        self.num = int(input("введите числитель"))
        self.den = int(input("введите знаменатель"))
        if self.den == 0:
            raise ValueError("знаменатель не может быть равен нулю")
    
    def __str__(self):
        return f"{self.num}/{self.den}"


a1 = Fraction()
print(a1)

a2 = Fraction(6, 7)
print(a2)

a3 = Fraction()
a3.input()
print(a3)
