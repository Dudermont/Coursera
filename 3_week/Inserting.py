s = r = input()
y = len(s)
count = 0
while count != y:
    q = s[:count * 2]
    r = s.replace(q, q + '*', 1)
    s = r
    count += 1
print(s[1:])
