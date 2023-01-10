start_roasted = open('input.txt', 'r', encoding='utf-8')
parties, votes = [], []
a = 0
for line in start_roasted:
    if line != 'PARTIES:\n' and line != 'VOTES:\n' and a == 0:
        parties.append(line.strip())
        votes += [0]
    if a == 1:
        votes[parties.index(line.strip())] += 1
    if line == 'VOTES:\n':
        a = 1
pv = list(map(lambda x, y: [x, y], votes, parties))

pv.sort(key=lambda x: [-x[0], x[1]])
for i in range(len(pv)):
    print(pv[i][1], sep='\n')
