import math

a = float(input())
b = float(input())
c = float(input())

d = (b ** 2) - (4 * a * c)
if a != 0:
    if d > 0:
        x1 = ((0 - b) - math.sqrt(d)) / (2 * a)
        x2 = ((0 - b) + math.sqrt(d)) / (2 * a)
        if x2 < x1:
            print(x2, x1)
        else:
            print(x1, x2)
    elif d == 0:
        x = -b / (2 * a)
        print(x)
    else:
        print()
