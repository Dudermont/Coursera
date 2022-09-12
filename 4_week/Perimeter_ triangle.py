x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())


def distance(a, b, c, d):
    kat1 = c - a
    kat2 = d - b
    gip = kat1 ** 2 + kat2 ** 2
    return gip ** (1 / 2)


def perimeter(a, b, c, d, e, f):
    p = distance(a, b, c, d) + distance(c, d, e, f) + distance(a, b, e, f)
    return p


print(perimeter(x1, y1, x2, y2, x3, y3))
