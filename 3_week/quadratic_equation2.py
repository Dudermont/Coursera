import math

a = float(input())
b = float(input())
c = float(input())

d = (b ** 2) - (4 * a * c)
if a == b == 0:
    if b != c:
        print(0)
    else:
        print(3)
elif a != 0:
    if d > 0:
        x1 = ((0 - b) - math.sqrt(d)) / (2 * a)
        x2 = ((0 - b) + math.sqrt(d)) / (2 * a)
        if x2 < x1:
            print(2, x2, x1)
        else:
            print(2, x1, x2)
    elif d == 0:
        x = -b / (2 * a)
        print(1, x)
    else:
        print(0)
else:
    x = -c / b
    print(1, x)
