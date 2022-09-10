a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())


la = (a * d) - (b * c)

if la == 0:
    print(0)
else:
    lx = (e * d) - (f * b)
    ly = (a * f) - (e * c)
    x = lx / la
    y = ly / la
    print(x, y)
