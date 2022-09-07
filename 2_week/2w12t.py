x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

x = x1 % 2 == y1 % 2
y = x2 % 2 == y2 % 2

if 0 < x1 < 9 and 0 < y1 < 9 and 0 < x2 < 9 and 0 < y2 < 9:
    if y1 < y2:
        if x == y:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

else:
    print('NO')
