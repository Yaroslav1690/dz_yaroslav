x = int(input("Введите первое число X"))
y = int(input("Введите второе число Y"))
if x > 0 and y > 0:
    print("это первая четверть")
elif x < 0 and y > 0:
    print("это вторая четверть")
elif x < 0 and y < 0:
    print("это третья четверть")
elif x > 0 and y < 0:
    print("это четвертая четверть")
elif y == 0:
    print("Точка лежит на оси X")
elif x == 0:
    print ("Точка лежит на оси Y")