n = int(input())
m = int(input())
k = int(input())


x = n * m
e = k % n
c = k % m
if k > 0 and m > 0 and n > 0:
    if k > x:
        print('NO')
    elif e == 0 or c == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
