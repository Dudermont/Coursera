a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

res = 0
v1 = (a1 // a2) * (b1 // b2) * (c1 // c2)
v2 = (a1 // a2) * (b1 // c2) * (c1 // b2)
v3 = (a1 // b2) * (b1 // a2) * (c1 // c2)
v4 = (a1 // b2) * (b1 // c2) * (c1 // a2)
v5 = (a1 // c2) * (b1 // a2) * (c1 // b2)
v6 = (a1 // c2) * (b1 // b2) * (c1 // a2)

if v1 > res:
    res = v1
if v2 > res:
    res = v2
if v3 > res:
    res = v3
if v4 > res:
    res = v4
if v5 > res:
    res = v5
if v6 > res:
    res = v6

print(res)
