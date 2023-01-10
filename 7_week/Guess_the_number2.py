n = int(input())
diapason = set(range(1, n + 1))
set_beatrice = set()
r = ''
answer = []
while r != 'HELP':
    r = input()
    if r != 'HELP':
        set_beatrice = set(map(int, r.split()))
    if 2 * len(diapason & set_beatrice) > len(diapason) and r != 'HELP':
        answer.append('YES')
        diapason &= set_beatrice
        set_beatrice = set()
    elif 2 * len(diapason & set_beatrice) <= len(diapason) and r != 'HELP':
        answer.append('NO')
        diapason -= set_beatrice
        set_beatrice = set()
for i in answer:
    print(i)
print(*sorted(diapason))
