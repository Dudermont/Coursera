def sum(a, n):
    if n == 0:
        return a
    return sum(a, n - 1) + 1


a = int(input())
n = int(input())
print(sum(a, n))
