import math


def IsPointInSquare(x, y):
    return math.sqrt(x ** 2) + math.sqrt(y ** 2) <= 1


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
