from random import randint
b = randint(0, 100)
a = int(input("загадайте число"))
while a != b:
    a = int(input("повторите попытку"))
    if a < b:
        print("загаданное число больше")
    elif a > b:
        print("загаданное число меньше")
    else:
        print("вы угадали число!")
    
