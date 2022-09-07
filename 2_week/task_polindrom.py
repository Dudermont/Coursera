K = int(input())
x = 1
count = 0

while x <= K:
    while x != 0:
        c = x % 10
        print(c, end='')
        x = x // 10
    if c == x:
        count = count + 1
    x = x + 1
    print(count)
