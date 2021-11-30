d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
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
assert poisk([1, 2, 3, 4, 5, 6, 7, 8, 9], 0) == None
assert poisk([1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9], 1) == 0