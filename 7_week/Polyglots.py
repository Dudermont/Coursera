with open('input.txt', 'r', encoding='utf8') as inF:
    line, lines = int(inF.readline()), inF.readlines()
k, c, Sl, Cl = 1, int(lines[0]), [], set()
for i in range(line):
    school = set()
    while k < c + 1:
        school.add(*tuple(lines[k].split()))
        k += 1
    Sl.append(school)
    Cl |= Sl[i]
    Sl[0] &= Sl[i]
    if k < len(lines) - 1:
        c = int(lines[k]) + k
        k += 1
print(len(Sl[0]), *Sl[0], len(Cl), *Cl, sep='\n')
