in_file = open('input.txt')
words_dict = dict()
value_list = []
for line in in_file:
    lines = line.split()
    for elem in lines:
        if elem not in words_dict:
            words_dict[elem] = 0
        value_list.append(words_dict[elem])
        words_dict[elem] += 1
print(*value_list)
in_file.close()