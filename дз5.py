d = [3, 7, 1, 8, 5, 9, 2, 4, 6]
d = sorted(d)
def poisk(d, a):
    low = 0
    high = len(d) - 1
    while low <= high:
        mid = (low + high) // 2
        if d[mid] == a:
            return mid
        elif d[mid] > a:
            high = mid - 1
        elif d[mid] < a:
            low = mid + 1
    return None



a = int(input("Введите искомый элемент: "))
print(poisk(d, a))
assert poisk([], 6) == None
assert poisk([3, 7, 1, 8, 5, 9, 2, 4, 6], 0) == None
assert poisk([3, 7, 1, 3, 1, 8, 7, 8, 5, 9, 4, 6, 2, 4, 6], 8) == 5