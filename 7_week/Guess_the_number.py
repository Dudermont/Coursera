n = int(input())
diapason = set(range(1, n))
b = set()
r = ''
while r != 'HELP':
    r = input()
    if r != 'YES' and r != 'NO' and r != 'HELP':
        b = set(map(int, r.split()))
    if r == 'YES':
        diapason &= b
        b = set()
    if r == 'NO':
        diapason -= b
        b = set()
print(*sorted(diapason))
