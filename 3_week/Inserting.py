s = input()
y = len(s)
count = 0
while count != y - 1:
    q = r[:count + 1]
    r = r.replace(q, q + '*')
    count += 1
    print(r)


# i = s.find('h')
# r = s[::-1]
# z = r.find('h')
# j = y - z - 1
# c = s[i + 1:j]
#
# print(s[:i + 1], c.replace('h', 'H'), s[j:], sep='')
