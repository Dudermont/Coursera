import math


def MinDivisor(n):
    count = 2
    x = math.sqrt(n)
    while count <= x:
        if n % count == 0:
            return count
        count += 1
    return 1


n = int(input())
if MinDivisor(n) != 1:
    print(MinDivisor(n))
else:
    print(n)
