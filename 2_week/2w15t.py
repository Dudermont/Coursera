a, b, c = int(input()), int(input()), int(input())

if a > b or a > c or b > c:
    if a > b or b > c:
        if b > c:
            (b, c) = (c, b)
            if a > b:
                (a, b) = (b, a)
                if b > c:
                    (b, c) = (c, b)
                    print(a, b, c)
                else:
                    print(a, b, c)
            else:
                print(a, b, c)
        elif a > b:
            (a, b) = (b, a)
            if b > c:
                (b, c) = (c, b)
                print(a, b, c)
            else:
                print(a, b, c)
        else:
            print(a, b, c)
    elif a >= c:
        (b, c) = (c, b)
        if a > b:
            (a, b) = (b, a)
            print(a, b, c)
        else:
            print(a, b, c)

else:
    print(a, b, c)
