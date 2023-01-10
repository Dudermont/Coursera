in_file = open('input.txt', 'r', encoding='utf-8')
out_file = open('output.txt', 'w', encoding='utf-8')
candidate_dict = {}
candidate_list = []
count = 0
for line in in_file:
    candidate = line.strip()
    candidate_dict[candidate] = candidate_dict.get(candidate, 0) + 1
    count += 1
count2 = 0
count3 = 0
for elem in candidate_dict:
    candidate_list.append((candidate_dict[elem], elem))
for elem in sorted(candidate_list, reverse=True):
    if elem[0] > count / 2:
        print(elem[1], file=out_file)
        count3 += 1
    else:
        if count2 == 2 or count3 == 1:
            break
        else:
            print(elem[1], file=out_file)
            count2 += 1
in_file.close()
out_file.close()
