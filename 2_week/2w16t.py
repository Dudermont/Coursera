a, b, c = int(input()), int(input()), int(input())

if a == b or a == c or b == c:
    if a != b:
        if a != c:
            if b != c:
                print('0')
        if b != c:
            print('2')
        else:
            print('2')
    elif a != c:
        if b != c:
            print('2')
        else:
            print('2')
    elif b != c:
        print('2')
    else:
        print('3')

else:
    print('0')
