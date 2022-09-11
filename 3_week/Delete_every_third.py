s = input()
y = len(s)
count = 0
while count != y:
    if count % 3 != 0:
        print(s[count], sep='', end='')
    count += 1
