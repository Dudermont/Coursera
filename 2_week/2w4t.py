x = int(input())
y = x % 4
c = x % 100
t = x % 400
if y == 0 and c != 0 or t == 0:
    print('YES')
else:
    print('NO')
