k = input()
a = k.count("(")
b = k.count(")")
if a > b:
    print("не хватает закрывающей скобки", a - b)
elif a < b:
    print("не хватает открывающей скобки", b - a)
else:
    print("все верно")