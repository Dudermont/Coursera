z = int(input())
c = int(input())
if c > z:
    f = c
    s = z
else:
    f = z
    s = c

while z != 0:
    z = int(input())
    if z >= f:
        s = f
        f = z
    elif z >= s:
        s = z
print(s)
