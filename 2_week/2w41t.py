A = int(input())
c = 1
f0 = 0
f1 = 1
f2 = f0 + f1
while f2 < A:
    f2 = f0 + f1
    f0, f1 = f1, f2
    c += 1
if A == 0:
    print(0)
elif A != f2:
    print(-1)
else:
    print(c)
