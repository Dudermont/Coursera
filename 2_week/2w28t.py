N = int(input())

x = 1
r = 1
while r != N:
    r = x * 2
    x = r
    if r > N:
        print('NO')
        break
if r == N:
    print('YES')
