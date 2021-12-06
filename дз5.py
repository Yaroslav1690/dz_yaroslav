d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def poisk(d, a):
    low = -1
    high = len(d) - 1
    while low < high - 1:
        mid = (low + high) // 2
        if d[mid] >= a:
            high = mid
        else:
            low = mid
    if high >= 0 and d[high] == a:
        return high
    else:
        return None

    


a = int(input("Введите искомый элемент: "))
print(poisk(d, a))
assert poisk([], 6) is None
assert poisk([1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9], 1) == 0
assert poisk([5, 5, 5, 5, 5], 5) == 0
assert poisk([], 42) is None
assert poisk([0], 0) == 0
assert poisk([0], 1) is None
assert poisk([-1, 0, 42], 0) == 1
assert poisk([-42, 0, 42], 42) == 2
assert poisk([-6, -5, -4, -3, -2, -1], -4) == 2
assert poisk([1, 2, 3, 4, 5, 6], 4) == 3
assert poisk([1, 2, 3, 4, 5, 6, 7], 4) == 3
assert poisk([1, 2, 3, 4, 5], 7) is None
assert poisk([1, 2, 3, 4, 5, 6], 7) is None
assert poisk([-2, -2, -1, 0, 1, 2, 2, 2], -1) == 2
assert poisk([-2, -2, -1, 0, 1, 1, 2, 2], 4) is None
assert poisk([42, 42, 42, 42, 42], 42) == 0
assert poisk([-42, -42, -42, -42, -42], -42) == 0