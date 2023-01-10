in_file = open('input.txt')
candidate_dict = {}
for line in in_file:
    cand = line.split()
    candidate_dict[cand[0]] = candidate_dict.get(cand[0], 0) + int(cand[1])
for elem in sorted(candidate_dict):
    print(elem, candidate_dict[elem])
in_file.close()
