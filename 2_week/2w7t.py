a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

x = a1 % 2 == b1 % 2
y = a2 % 2 == b2 % 2
if x == y:
    print('YES')
else:
    print('NO')
