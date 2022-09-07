N = int(input())
a = N//60 % 24
b = (N - (N//60)*60) % 60
print(a, b)
