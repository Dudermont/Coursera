import math


def lagrange(n, q):
    sqrtn = int(math.sqrt(n))
    if n - sqrtn ** 2 == 0:
        return str(sqrtn)
    if q == 1:
        return 0
    while lagrange(n - sqrtn ** 2, q - 1) == 0:
        sqrtn -= 1
        if sqrtn <= 0:
            return 0
    return str(sqrtn) + ' ' + lagrange(n - sqrtn ** 2, q - 1)


n = int(input())
print(lagrange(n, 4))
