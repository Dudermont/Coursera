def IsPointInArea(x, y):
    line1 = (0 + 1) * (y - 0) - (x + 1) * (2 - 0)
    line2 = (0 + 1) * (y - 1) - (x + 1) * (0 - 1)
    r = ((-1 - x) ** 2 + (1 - y) ** 2) ** 0.5
    return (line1 >= 0 and line2 >= 0 and r <= 2 or
            line1 <= 0 and line2 <= 0 and r >= 2)


x = float(input())
y = float(input())
if IsPointInArea(x, y):
    print('YES')
else:
    print('NO')
