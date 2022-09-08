import math

x = float(input())
full = math.floor(x)
af_dot = int((x - full) * 10)

if af_dot < 5:
    z = math.floor(x)
else:
    z = math.ceil(x)
print(z)
