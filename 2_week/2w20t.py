k = int(input())

x = k / 3
y = k / 5
z = k % 3
c = k % 5

if k > 10:
    print('YES')
elif z == 0 or c == 0:
    print('YES')
else:
    print('NO')
