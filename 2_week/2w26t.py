a = int(input())

z = 2
x = a % z
while x != 0:
    z = z + 1
    x = a % z
print(z)
