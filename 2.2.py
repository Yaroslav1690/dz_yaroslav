from math import gcd


class Fraction: 
        def __init__(self, top=0, bottom=1): 
            self.num = top 
            self.den = bottom 

        def input(self): 
            self.num = int(input("Введите числитель: "))        
            self.den = int(input("Введите знаменатель: "))  
            if self.den == 0: 
                print("error")

        def __str__(self):
            return f"{self.num}/{self.den}"
 
        def reduce(self): 
            c = gcd(self.num, self.den) 
            self.nom = self.num // c
            self.den = self.den // c

class IrreduceadFraction(Fraction): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reduce()

    def input(self, *args, **kwargs) -> None:
        super().input(*args, **kwargs)
        self.reduce()
      
      
