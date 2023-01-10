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
p = list(map(lambda x: x / sum(votes), votes))
for i in range(len(parties)):
    if p[i] >= 0.07:
        print(parties[i], sep='\n')
