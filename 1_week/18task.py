N = int(input())
a = N // 3600 % 24
b = str(N // 600 % 6) + str(N // 60 % 10)
c = str(N % 60 // 10) + str(N % 60 % 10)
print(a, b, c, sep=':')
