def move(n, x, y):
    if n == 1:
        print(1, x, y)
    else:
        trans = 6 - x - y
        move(n - 1, x, trans)
        print(n, x, y)
        move(n - 1, trans, y)


n = int(input())
move(n, 1, 3)
