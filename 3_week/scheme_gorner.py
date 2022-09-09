n = int(input())
x = float(input())
total = 0
while n >= 0:
    a = float(input())
    c = 0
    x_n = 1
    while c < n:
        x_n = x_n * x
        c = c + 1
    a_x = a * x_n
    n = n - 1
    total = total + a_x
print(total)
