a = str(input("Введите элемент"))
b = list()
while a != '':
    b.append(a)
    a = str(input())
else:
    print(b)