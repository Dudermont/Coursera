z = int(input())
x = 0
c = 0
while z != 0:
    if z > x:
        c = 1
        x = z
        z = int(input())
    elif z == x:
        c += 1
        z = int(input())
    else:
        z = int(input())
print(c)
