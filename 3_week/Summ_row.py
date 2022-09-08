n = int(input())
count = 1
x = 0

while count <= n:
    x = x + (1 / (count ** 2))
    count = count + 1

print('{0:.6f}'.format(x))
