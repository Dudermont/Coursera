x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def distance(a, b, c, d):
    kat1 = c - a
    kat2 = d - b
    gip = kat1 ** 2 + kat2 ** 2
    return gip ** (1 / 2)


print(distance(x1, y1, x2, y2))
