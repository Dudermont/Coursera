A = int(input())
B = int(input())
C = int(input())

a1 = A % 2
b1 = B % 2
c1 = C % 2

if a1 == 1 or b1 == 1 or c1 == 1:
    if a1 == 0 or b1 == 0 or c1 == 0:
        print('YES')
    else:
        print('NO')
elif a1 == 0 or b1 == 0 or c1 == 0:
    if a1 == 1 or b1 == 1 or c1 == 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
