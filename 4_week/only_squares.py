import math


def only_sqrt():
    n = int(input())
    if n != 0:
        if int(math.sqrt(n)) ** 2 == n:
            only_sqrt()
            print(n, end=' ')
            return 1
        else:
            return only_sqrt()
    return 0


if only_sqrt() == 1:
    print()
else:
    print(0)
