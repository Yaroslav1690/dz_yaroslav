a = []
b = input()
k = int(input())
for i in b:
    if i.isdigit():
        a.append(i)
print(k, '-ая цифра в строке', a[k - 1])