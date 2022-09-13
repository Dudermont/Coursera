def xor(x, y):
    return (x > 0 and x != y or
            y > 0 and x != y)

x = int(input())
y = int(input())
if xor(x, y):
    print(1)
else:
    print(0)
