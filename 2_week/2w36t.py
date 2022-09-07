z = int(input())
c = 0
while z != 0:
    x = z % 2
    if x == 0:
        c += 1
    z = int(input())

print(c)
