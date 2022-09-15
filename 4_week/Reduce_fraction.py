def gcd(n, m):
    if n % m == 0:
        return m
    return gcd(m, n % m)


def ReduceFraction(n, m):
    p = n // gcd(n, m)
    q = m // gcd(n, m)
    return p, q


n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
