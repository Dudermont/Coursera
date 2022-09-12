def min4(n1, n2, n3, n4):
    x = min(n1, n2)
    y = min(n3, n4)
    return min(x, y)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))
