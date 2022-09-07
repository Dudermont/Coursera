A = int(input())
B = int(input())

while B != A:
    x = A % 2
    if x == 0:
        if (A / 2) >= B:
            A = A / 2
            print(':2')
        else:
            A = A - 1
            print('-1')
    else:
        A = A - 1
        print('-1')
