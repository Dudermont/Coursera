z = int(input())
c = 0
while z != 0:
    x = z
    z = int(input())
    if z > x:
        c += 1

print(c)
