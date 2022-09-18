def lagrange(n, q):
    if q == 0:
        return 0
    cube = int(n ** (1 / 3))
    if n - cube ** 3 == 0:
        return str(cube ** 3)
    while cube > 0:
            if lagrange(n - cube ** 3, q - 1):
                return str(cube ** 3) + ' ' + lagrange(n - cube ** 3, q - 1)
            cube -= 1
    return 0


n = int(input())
print(lagrange(n, 7))
