import math

x = float(input())

rub = math.floor(x)
cop = round((x - rub) * 100)
print(rub, cop)
