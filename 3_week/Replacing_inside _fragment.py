s = input()
y = len(s)
i = s.find('h')
r = s[::-1]
z = r.find('h')
j = y - z - 1
c = s[i + 1:j]

print(s[:i + 1], c.replace('h', 'H'), s[j:], sep='')
