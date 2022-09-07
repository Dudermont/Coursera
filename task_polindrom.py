K = int(input())
x = 1
count = 0

while x <= K:
    z = x
    c = 0

    while z != 0:
        c = c * 10 + z % 10
        z = z // 10
    if c == x:
        count = count + 1
    x = x + 1
print(count)
