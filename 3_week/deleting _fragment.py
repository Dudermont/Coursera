s = input()

y = len(s)
i = s.find('h')
r = s[::-1]
z = r.find('h')
c = i + z + 1
j = y - z

print(s[:i], s[j:], sep='')
