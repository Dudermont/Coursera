def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


a = int(input())
b = int(input())
print(gcd(a, b))
