a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

la = (a * d) - (b * c)
lx = (e * d) - (f * b)
ly = (a * f) - (e * c)

if la == 0:
    if a == b == c == d == e == f == 0:
        print(5)
    elif lx != 0 or ly != 0 or (a == b == c == d == 0 and (e != 0 or f != 0)):
        print(0)
    elif (b == 0 and a != 0) or (d == 0 and c != 0):
        if b == 0 and a != 0:
            x = e / a
            print(3, x)
        elif d == 0 and c != 0:
            x = f / c
            print(3, x)
    elif (a == 0 and b != 0) or (c == 0 and d != 0):
        if a == 0 and b != 0:
            y = e / b
            print(4, y)
        elif c == 0 and d != 0:
            y = f / d
            print(4, y)
    else:
        if d == 0:
            p = -a / b
            q = e / b
            print(1, p, q)
        elif b == 0:
            p = -c / d
            q = f / d
            print(1, p, q)
        else:
            p = -a / b
            q = e / b
            print(1, p, q)
else:
    lx = (e * d) - (f * b)
    ly = (a * f) - (e * c)
    x = lx / la
    y = ly / la
    print(2, x, y)
