def power(a, n):
    if a == 0:
        return 1
    if n == 0:
        return 1
    count = 1
    x = a
    if n > 0:
        while count != n:
            x = x * a
            count += 1
        return x
    if n < 0:
        while count != n:
            x = x / a
            count -= 1
        return x


a = float(input())
n = int(input())
print(power(a, n))
