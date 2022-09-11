s = input()
y = len(s)
i = s.find('f')
r = s[i + 1:]
z = r.find('f')
j = i + z + 1
if i < 0:
    print(-2)
if i >= 0:
    if z < 0:
        print(-1)
    else:
        print(j)
