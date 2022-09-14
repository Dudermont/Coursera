def power(a, n):
    if n <= 1:
        return a ** n
    else:
        return a * power(a, n - 1)


a = float(input())
n = int(input())
print(power(a, n))
