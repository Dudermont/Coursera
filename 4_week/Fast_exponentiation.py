def power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power(a * a, n / 2)
    return a * power(a * a, (n - 1) / 2)


a = float(input())
n = int(input())
print(power(a, n))
