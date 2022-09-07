a = int(input())
b = int(input())

y = b - a + 1
x = b // y
c = y * x
if b == c:
    print('YES')
else:
    print('NO')
