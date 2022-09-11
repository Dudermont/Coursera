s = input()

y = len(s)
in1 = s.find('f')
r = s[::-1]
z = r.find('f')
c = in1 + z + 1
im2 = y - z - 1

if in1 >= 0:
    if (y > 1) and (c != y):
        print(in1, im2)
    elif (y > 1) and (c == y):
        print(in1)
    else:
        if in1 >= 0:
            print(in1)
