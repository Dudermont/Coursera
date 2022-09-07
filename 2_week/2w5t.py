a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if 0 < a1 and b1 and a2 and b2 < 9:
    x = a1 - a2
    y = b1 - b2
    if -1 <= x <= 1 and -1 <= y <= 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
