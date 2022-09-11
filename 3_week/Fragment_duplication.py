s = input()
y = len(s)
i = s.find('h')
r = s[::-1]
z = r.find('h')
j = y - z - 1
print(s[:j], s[i + 1:j], s[j:], sep='')
