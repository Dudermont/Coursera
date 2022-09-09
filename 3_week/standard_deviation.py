import math

x = int(input())
count = 0
xsum = 0
xqd = 0
while x != 0:
    xsum = xsum + x
    xqd = xqd + (x ** 2)
    count += 1
    x = int(input())
sqd = xsum ** 2
s1 = sqd / count
s2 = xqd - s1
s = s2 / (count - 1)
q = math.sqrt(s)

print(q)
