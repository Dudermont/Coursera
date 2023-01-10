in_file = open('input.txt')
word_dict = {}
word_list = []
for line in in_file:
    words = line.split()
    for elem in words:
        word_dict[elem] = word_dict.get(elem, 0) + 1
for elem in word_dict:
    word_list.append((-word_dict[elem], elem))
for i in sorted(word_list):
    print(i[1])
in_file.close()
